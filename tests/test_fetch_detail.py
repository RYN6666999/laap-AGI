"""A庫細節取回的回歸閘（V1.6，2026-08-20）。

為什麼存在：V1.5 的 13/13 是現寫的 heredoc，跑完就消失。
下次有人改 _fetch_detail，沒有東西會告訴他打壞了什麼 —— 那正是這份 code
一整晚在防的「靜默退化」，而驗證本身就是靜默的。這個檔把它變成閘。

紅線（V1.6 §20）：
  · 不連網、不打 live 服務、不碰 live A庫
  · 資料凍結在 tests/fixtures/memory_fixture.json
  · 唯一外部依賴是 jieba（_fetch_detail 本來就需要）

對 V1.6 §18 的偏離（刻意）：
  工單說「從 A庫抽一小撮代表性列」。不能照做 —— laap-AGI 是公開 repo，
  而工單點名的兩筆記憶含真實金融機構與客戶姓名。
  改用合成 fixture：同樣的判準形狀，零真實資訊。
  測的是演算法行為，本來就不需要真人資料。

跑：pytest tests/test_fetch_detail.py -q
"""
import json
import sqlite3
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_REPO = _HERE.parent
sys.path[:0] = [str(_REPO / "aris_brain"), str(_REPO),
                str(_REPO.parent / "neuralis")]

pytest.importorskip("jieba", reason="中文關鍵字腳需要 jieba")
import aris_cognitive_bridge as B  # noqa: E402


@pytest.fixture(scope="module")
def fixture_db(tmp_path_factory):
    """把凍結的 JSON 建成一個臨時 sqlite，schema 與 A庫 相同的必要欄位。"""
    data = json.loads((_HERE / "fixtures" / "memory_fixture.json").read_text("utf-8"))
    db = tmp_path_factory.mktemp("aris") / "memory.sqlite"
    conn = sqlite3.connect(db)
    conn.execute("""CREATE TABLE memories(
        id INTEGER PRIMARY KEY, source TEXT, created_at REAL,
        content TEXT, flagged INTEGER, total_recalls INTEGER)""")
    conn.executemany("INSERT INTO memories VALUES (?,?,?,?,?,?)", data["rows"])
    conn.commit()
    conn.close()
    return db


@pytest.fixture(autouse=True)
def point_at_fixture(fixture_db, monkeypatch):
    """把 _fetch_detail 指向 fixture，確保永遠不會碰到 live A庫。"""
    monkeypatch.setattr(B, "ARIS_MEMORY_DB", Path(fixture_db))


def ids(hits):
    return [h[0] for h in hits]


# ── 正面：三條命中路徑 ────────────────────────────────────────

def test_識別碼命中():
    """3 位以上數字是強證據，一個就夠。"""
    assert 103 in ids(B._fetch_detail("79800 這個數字出現在哪？"))


def test_識別碼下限是三位數():
    """守 _KEY_RE 的 {3,}。查詢刻意只留數字 ——
    若寫成「訂單 482 出貨了嗎」，中文詞「訂單/出貨」會代打，
    正則被改成 {5,} 也照樣過，這一案就白守了。"""
    cjk = [w for w in B._query_words("482") if any("一" <= c <= "鿿" for c in w)]
    assert cjk == [], f"查詢不可含中文實詞，否則中文腳會代打：{cjk}"
    assert 113 in ids(B._fetch_detail("482"))


def test_專名單詞命中_紫貘():
    """user-dict 專名 = 強證據。jieba 原生會把「紫貘」切成 紫+貘。"""
    hits = ids(B._fetch_detail("紫貘後面的數字最近一次是多少？"))
    assert hits and set(hits) <= {101, 102}


def test_專名單詞命中_C單():
    assert 103 in ids(B._fetch_detail("C 單的課程費用是多少？"))


def test_中文實詞兩個以上命中():
    """光年銀行/星芒租賃是虛構名。拆詞後至少 2 個實詞落在同一筆才算。"""
    assert 104 in ids(B._fetch_detail("光年銀行拒絕貸款那件事"))


def test_恰好兩個實詞就算命中():
    """守 _WORD_MIN_HITS == 2。「門市」「盤點」剛好 2 個 ——
    門檻若被改成 3，這一案立刻紅。"""
    assert 111 in ids(B._fetch_detail("門市的盤點在哪裡看"))
    # 正對照：確認真的只對上 2 個詞，否則這一案守不住門檻
    hit = [w for w in B._query_words("門市的盤點在哪裡看") if w in "門市的盤點紀錄要重做"]
    assert len(hit) == 2, f"這一案必須剛好 2 個實詞命中，實際 {hit}"


def test_單字不算實詞_不被長文誤撈():
    """守「單一中文字不算實詞」。#112 含大量「後」「面」單字。
    若拿掉那條過濾，問紫貘時會撈到 #112 而不是 101/102 ——
    這正是 2026-08-19 實測抓到的真 bug。"""
    # 不能用紫貘當查詢 —— 它是強證據，排序永遠壓過 #112，單字規則就測不到。
    # 改用沒有強證據的問法：只有「後」「面」這些單字可能對上 #112。
    assert B._fetch_detail("後面那個") == []
    assert B._fetch_detail("前面後面的東西") == []


def test_排序_近的優先():
    """兩筆紫貘記憶都符合時，時間近的（102）要排前面。"""
    hits = ids(B._fetch_detail("紫貘"))
    assert hits[0] == 102


# ── 反面：不存在的東西一律回空 ──────────────────────────────

@pytest.mark.parametrize("q", [
    "青鴉的代號是多少？",
    "赤梟後面的數字是多少？",
    "白獬那組編號是什麼？",
    "台北今天天氣如何",
])
def test_庫裡沒有就不注入(q):
    """幻覺防線：問一個不存在的東西，正確答案是「沒有」，
    不是「最接近的一筆」。"""
    assert B._fetch_detail(q) == []


def test_單一常見詞不構成命中():
    """青鴉那案靠這條守住 —— 光憑「代號」不撈，即使 fixture 裡有 4 筆含它。"""
    assert B._fetch_detail("代號") == []


def test_非真人來源不撈():
    """aris-self 是她自己寫的，不是地面資料。#110 含紫貘9999 但不該出現。"""
    assert 110 not in ids(B._fetch_detail("紫貘9999"))


@pytest.mark.parametrize("q", ["", "嗯", "   "])
def test_邊界輸入回空(q):
    assert B._fetch_detail(q) == []


# ── 不擋管線 ─────────────────────────────────────────────────

def test_DB不存在不拋例外(monkeypatch, tmp_path):
    """絕不擋認知管線：任何例外回 []（寫 log，不靜默）。"""
    monkeypatch.setattr(B, "ARIS_MEMORY_DB", tmp_path / "definitely-absent.db")
    assert B._fetch_detail("79800") == []


# ── 出處鍥格式 ───────────────────────────────────────────────

def test_出處鍥前後夾住編號():
    """引用規則綁在資料本身，不跟 context 後段的指令搶位置。
    實測：規則寫成獨立一行擺區塊尾巴 → LLM 遵守 0/3。"""
    out = B._format_detail(B._fetch_detail("79800"))
    assert "內容：" in out
    # 前夾：內容之前要先宣告編號
    head, _, tail = out.partition("內容：")
    assert "A庫#103" in head, "內容前要有編號宣告"
    # 後夾：內容之後要再標一次。實測（2026-08-19）規則只放尾巴時 LLM 遵守 0/3，
    # 前後夾住才是這個格式存在的理由 —— 少一邊就不是這個設計了。
    assert "A庫#103" in tail, "內容後要再標一次編號（前後夾）"


def test_沒命中回空字串():
    assert B._format_detail([]) == ""


# ── 人工驗收項（測不到就明說，不假裝測得到）─────────────────

@pytest.mark.skip(reason="人工驗收：需要真實 LLM + 檔案系統，測不了")
def test_記憶當線索不當答案():
    """V1.6 §32。實測（2026-08-19，Hermes + 真實 LLM）：
    問「C 單的課程費用」時，Aris 沒有複述記憶裡的數字，
    而是去重讀 C單狀態.json 逐筆確認才回答。
    這比帶編號的引用更有價值，但需要真實 LLM 與檔案系統，自動化測不到。
    每次改注入格式後，請人工重跑一次這個情境。"""
