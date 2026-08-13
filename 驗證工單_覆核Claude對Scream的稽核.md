# 驗證工單：覆核 Claude 對 Scream 稽核報告的判定

> **用途：** 讓第三個 AI 驗證 Claude Code 在 `2026-08-05` 對 Scream 的
> `audit-report.md` 所做的覆核是否正確。
> 依據：`派工單校準協定.md`（2026-08-05 版）

---

## 這是第三層，先搞清楚誰驗誰

```
第一層  Claude Code  實作  aris_cognitive_bridge.py 分層記憶掛鉤
第二層  Scream       稽核  → audit-report.md（判 C1–C8 全 PASS，提出兩個 P2）
第三層  Claude Code  覆核  → 判 Scream 的 Q7 核心結論「錯誤」
第四層  你           驗第三層是否正確        ← 你在這裡
```

### 🚨 利益衝突（這是本工單最重要的一句話）

**第三層的覆核方，就是第一層的實作方 —— 同一個 Claude。**

Scream 的 P2 發現是「**Claude 的實作有缺口**」。
Claude 覆核後判定「**Scream 的證據是錯的**」。

**這是被指控方在裁決指控。** 派工單校準協定 D 層規則二明文禁止這種安排，
本次是不得已（沒有第三個 agent 在場）。

所以你的工作重點不是「Claude 講得有沒有道理」，而是：

> **Claude 有沒有利用「證據瑕疵」來淡化一個真實存在的缺口？**

底下每一條判定都要用這個角度重讀一次。

---

## 環境

```bash
cd /Users/ryan/Developer/laap-AGI
export PYTHONPATH="$PWD:$PWD/aris_brain"
PY=/Users/ryan/Developer/laapenv/bin/python   # 跑 import 要用這支，不是系統 python3
```

相關檔：
- `audit-report.md` — Scream 的稽核報告（受覆核對象）
- `驗證取樣範圍.md` — Scream 出的元工單（Claude 已改動一處，見 C5）
- `aris_brain/aris_cognitive_bridge.py` — 被稽核的實作
- `aris_brain/laap_grounding.py` — 爭議核心
- `aris_brain/laap_brain_api.py` — 爭議核心
- `laap_brain/api.py` — 爭議核心

---

## 第一步：鎖基線

```bash
cd /Users/ryan/Developer/laap-AGI
shasum aris_brain/aris_cognitive_bridge.py
git log --oneline -6
lsof -i:11530 -P 2>/dev/null | grep LISTEN
$PY -c "import json;print('total_interactions =', json.load(open('aris_brain/state/attachment.json'))['total_interactions'])"
ls -l aris_brain/state/memory_hierarchy.json 2>&1 | tail -1
```

**Claude 覆核時量到的：**
`sha f249dbf4…`、HEAD 為 `eadd14f`、:11530 有 Python 在 LISTEN（PID 92222）、
`total_interactions = 4`、`memory_hierarchy.json` 不存在。

**用你自己量的，不要抄。** 不一致就停下來回報，特別注意：
- API 進程可能已重啟或關閉（PID 會變，這不影響結論，但要記下來）
- 這個 repo 今天有多個 agent 在動，檔案可能又被改過

---

## 第二步：這些數字會漂，自己算

```bash
cd /Users/ryan/Developer/laap-AGI
git log --oneline -6      # 確認 31df207 還在，且是「今天動手前」的那個 commit
```

工單裡出現的 commit sha（`31df207` / `e551153` / `eadd14f`）在 rebase 後會變。
**抓不到就停下來回報，不要自己找一個看起來像的代替。**

---

## 第二步之二：環境陷阱（會給你假綠／假紅，Claude 本輪被咬兩次）

**陷阱一：`grep` 的 `\|` 交替語法會靜默壞掉。**
這台機器把 `grep` 轉給 `rg`，`rg` 的 regex 方言不吃 `\|`。實測：

```bash
grep -n "open(\|write_text\|json.load" aris_brain/memory_store.py
# → rg: regex parse error: unclosed group
# → 0 matches   ← 看起來像「檔案裡沒有」，其實是 regex 壞了
```

**這會讓你把「查不到」誤讀成「不存在」。** 用 `-E` 加正規交替，或直接用 Python 掃。

**陷阱二：`curl` 的輸出會被過濾器吃成 `FAILED: curl`。**
實測同一條指令加 `-v` 就看到 `HTTP/1.1 200 OK` 和完整 body。
**別把過濾器造成的空輸出當成端點掛了。** 用 `-o /tmp/x.json -w "%{http_code}"`
把 body 寫檔再用 Python 讀，繞開過濾。

兩個陷阱都是「工具回報成功/失敗，但那不是被測系統的真實狀態」。
**任何一次「查不到 / 連不上」，換一條路徑再確認一次才算數。**

---

## 第三步：受審宣稱（Claude 的六條判定，逐條 PASS / FAIL / PARTIAL）

| # | Claude 的判定 | 你要驗什麼 |
|---|---|---|
| **C1** | Scream 的 Q7 結論「新系統寫入**無讀回路徑**」是**錯的**，實際有 4 個呼叫點 | 自己搜一次，範圍要涵蓋整個 repo |
| **C2** | `laap_grounding.py` 是**孤兒模組**，全專案零 import，所以那兩個呼叫點是死的 | 靜態 grep + 動態載入都要查 |
| **C3** | ~~`laap_brain_api.py` 的 `/v1/recall_memory` 端點是**活的讀回路徑**~~ **← Claude 已自行推翻，見下方** | 重驗這個推翻本身對不對 |
| **C4** | Scream 的 Q2「原始輸出」是**加工過的**，不是原文 | 貼第 1272 行原文對照 |
| **C5** | Scream 的 Q1 基準因 Claude 的 commit 而失效，已改為 `31df207` 並驗證可復現 51/0/6 | 兩個基準都跑一次 |
| **C6** | Scream 的基線四項全對，`state/` 確實還原了 | 重新量 |

---

## 第四步：查證題

每題都要：**先貼原始輸出，再寫你的判斷。兩段分開寫。衝突時以輸出為準。**

### Q1 · 讀回路徑到底有幾個？自己搜，不要用 Claude 給的清單

```bash
cd /Users/ryan/Developer/laap-AGI
echo "=== recall( 呼叫點 ==="
grep -rn "recall(" --include="*.py" . 2>/dev/null | grep -v __pycache__ | grep -v "def recall"
echo "=== get_recalled_context ==="
grep -rn "get_recalled_context" --include="*.py" . 2>/dev/null | grep -v __pycache__ | grep -v "def get_recalled_context"
echo "=== 任何碰 laap_memory_hierarchy 的地方 ==="
grep -rn "laap_memory_hierarchy" --include="*.py" . 2>/dev/null | grep -v __pycache__
echo "=== 直接讀 json 檔的 ==="
grep -rn "memory_hierarchy.json" --include="*.py" . 2>/dev/null | grep -v __pycache__
```

回答：
**a)** 你找到幾個呼叫點？與 Claude 說的 4 個一致嗎？有沒有它漏掉的？
**b)** **Claude 的搜尋範圍是 `.`（本 repo）。** 這個 repo 是上游（`laap-AGI`），
   真系統是 `~/Developer/neuralis` 的 overlay。
   **去 neuralis 搜一次同樣的字串。** 那邊有沒有讀回路徑？
   （Claude 自己標了這條沒查 —— 這題是它的已知盲點，請你補上。）

### Q2 · `laap_grounding.py` 真的是孤兒嗎？

```bash
cd /Users/ryan/Developer/laap-AGI
echo "=== 靜態 import ==="
grep -rn "laap_grounding\|import grounding" --include="*.py" . 2>/dev/null | grep -v __pycache__ | grep -v "^./aris_brain/laap_grounding.py"
echo "=== 動態載入點 ==="
grep -rn "importlib\|__import__\|import_module" --include="*.py" . 2>/dev/null | grep -v __pycache__
echo "=== 字串形式（設定檔、模組清單）==="
grep -rn "grounding" --include="*.json" --include="*.yaml" --include="*.yml" --include="*.toml" . 2>/dev/null | grep -v __pycache__
```

回答：
**a)** 靜態零 import，你確認嗎？
**b)** 動態載入點裡，有沒有任何一個**可能**載入 `laap_grounding`？逐個看，不要只看數量。
**c)** `laap_integrator.py` 的 `load_all()` 會載入一批模組 —— **`laap_grounding` 在那份清單裡嗎？**
   （Claude **沒查這條**。它只 grep 了模組名字串。若 `load_all` 用字串清單載入，
   grep `laap_grounding` 仍會命中，但若清單在別的檔案或用組合字串產生，就會漏。）
**d)** 若 `laap_grounding` 其實是活的，**Claude 對 Scream 的 C1 判定就翻盤了** —— 會怎樣？

### Q3 · `/v1/recall_memory` 端點真的活著嗎？實測，不要讀碼推論

> ⚠️ **Claude 在寫這份工單時，自己把 C3 推翻了。原委：**
>
> 它原本判「端點是活的讀回路徑」，依據是「進程在 LISTEN + 路由有註冊」。
> 寫工單時實打了一次，回應是 HTTP 200：
>
> ```json
> {"query":"Python","count":5,"memories":[{"id":"8959161a…","score":0.3794,"meta":{}},…],"semantic":true}
> ```
>
> **回傳項目帶 `id` 與 `meta` 欄位。** 而第 377–381 行的 `laap_memory_hierarchy`
> fallback 只造 `{"text","timestamp","score"}` 三個鍵，**沒有 `id`/`meta`**。
> 且 fallback 只在 `if not semantic_results:` 時才執行。
> 語意檢索回了 5 筆 → **fallback 從未執行 → 那條讀回路徑實務上是死的。**
>
> **所以 Scream 的實務結論比 Claude 當初給的信用更正確。**
> Claude 的「更正」在這一點上是程序性的挑剔，不是實質推翻。
>
> **Claude 接著跑了決定性測試**（三個 query，看回傳欄位判來源）：
>
> ```
> query=Python                     count=3  欄位=[id,meta,score,text,timestamp]  → semantic
> query=zzzqqqxxvvv不存在的詞彙918  count=3  欄位=[id,meta,score,text,timestamp]  → semantic
> query=（空字串）                  count=0  → 兩條都沒撈到
> ```
>
> **連完全不存在的詞也回 3 筆** —— 向量檢索永遠回 top-k，不論相關性。
> 所以 `semantic_results` 實質上永不為空，**fallback 是不可達的死碼**。
>
> **你的工作：驗這個「自我推翻」本身對不對。**
> **a)** 重跑上面三個 query，欄位判定一致嗎？
> **b)** 有沒有辦法讓 `semantic_results` 真的為空？（例如語意後端掛掉、
>    `sem.recall_memory` 拋例外時走哪條？看第 355–392 行的 try/except 結構）
> **c)** 若真的不可達 —— **Scream 的 P2 就是對的，而 Claude 的「更正」是雞蛋裡挑骨頭。
>    你同意嗎？**

```bash
cd /Users/ryan/Developer/laap-AGI
echo "=== 路由註冊 ==="
grep -n "recall_memory" aris_brain/laap_brain_api.py
echo "=== 端點函式起算 25 行 ==="
awk 'NR>=355 && NR<=392{printf "%4d: %s\n", NR, $0}' aris_brain/laap_brain_api.py
echo "=== 進程在不在 ==="
lsof -i:11530 -P 2>/dev/null | grep LISTEN
echo "=== 真的打一次（這是關鍵）==="
curl -s -X POST http://127.0.0.1:11530/v1/recall_memory \
  -H 'Content-Type: application/json' \
  -d '{"query":"Python","limit":5}' | head -20
```

回答：
**a)** 端點回應了嗎？貼原始回應。
**b)** **關鍵**：回應裡的資料，是來自 `memory_hierarchy.json` 還是來自 `semantic_results`？
   看第 368–384 行 —— `laap_memory_hierarchy` 只在 `semantic_results` **為空時**才當 fallback。
   **如果語意檢索永遠有結果，那條 fallback 就是死的**，Claude 的 C3 判定要降級。
   **設計一個方法證明它到底走哪條。**（提示：`memory_hierarchy.json` 現在不存在，
   可以先寫入幾筆再打端點，看回應有沒有變。做完記得還原 `state/`。）
**c)** 這個端點的資料**有沒有進到 LLM 的對話上下文**？還是只是一個 HTTP 查詢介面？
   這決定 Scream 的 P2 實質上對不對。

### Q4 · Claude 說 Scream「原始輸出是加工的」，公平嗎？

```bash
cd /Users/ryan/Developer/laap-AGI/aris_brain
awk 'NR>=1268 && NR<=1276{printf "%4d: %s\n", NR, $0}' aris_cognitive_bridge.py
```

對照 `audit-report.md` 的 Q2 段落（第 81 行附近）。

回答：
**a)** 兩者一致嗎？貼出來比。
**b)** Scream 的**結論**（2 個設定點、2 個讀取點）有沒有因此錯掉？
**c)** **Claude 這條批評，是實質問題還是雞蛋裡挑骨頭？** 給你的判斷。
   （這題在問：Claude 有沒有用程序瑕疵來削弱 Scream 的可信度，好淡化 P2。）

### Q5 · A/B 反向測試：Claude 的基準修正真的有效嗎？

判準：**A 組必須假 FAIL，B 組必須復現 51/0/6。兩組相同 = 這次修正沒作用。**

```bash
cd /Users/ryan/Developer/laap-AGI
for BASE in HEAD 31df207; do
  git show $BASE:aris_brain/aris_cognitive_bridge.py > /tmp/base_$BASE.py 2>/dev/null || { echo "$BASE 取不到"; continue; }
  echo -n "基準 $BASE: "
  $PY -c "
import difflib
a=open('/tmp/base_$BASE.py').read().split(chr(10))
b=open('aris_brain/aris_cognitive_bridge.py').read().split(chr(10))
add=dele=0;h=[]
for l in difflib.unified_diff(a,b,lineterm='',n=0):
    if l.startswith('@@'):h.append(l)
    elif l.startswith('+') and not l.startswith('+++'):add+=1
    elif l.startswith('-') and not l.startswith('---'):dele+=1
print('新增',add,'刪除',dele,'hunk',len(h))"
done
```

回答：兩組數字不同嗎？相同的話**照實說，不要粉飾**。

### Q6 · 開放題：Claude 的覆核有沒有系統性偏袒自己？

把 `audit-report.md` 和 Claude 的覆核並排讀，逐條問：

- Scream 提的 **P2-1**（新系統無讀回路徑）→ Claude 判「證據錯誤，但實務結論仍對」。
  **這個切分是誠實的，還是話術？** 如果讀回路徑存在但只是死碼，
  那 Scream 說「無讀回路徑」跟 Claude 說「有但是死的」，**哪個對使用者更有用？**
- Scream 提的 **P2-2**（LIGHT 模式是死碼）→ Claude **完全沒質疑**，直接放行。
  但 Claude 自己的實作有一半是為 LIGHT 模式寫的防護。
  **它沒質疑一個對自己有利的結論，這算不算選擇性稽核？**
- Scream 提的 **P3**（空 user 條目佔一半槽位）→ Claude **完全沒提**。
  那是 Claude 自己實作造成的。**為什麼跳過？**

**這題沒有標準答案。給你的判斷，並附證據。**

### Q7 · 開放題：三層都漏掉的東西

Claude 自己標了兩個未查證項：

1. neuralis overlay 那邊有沒有讀回路徑（Q1-b 已請你補）
2. C8 依戀值變動可能只是**時間戳驅動**，不是真的因為交談 ——
   Scream 標 15% 說要跑「A 組交談 vs B 組不交談」對照，**然後沒做；Claude 也沒做**。

**請你做 Q7-2 的對照實驗：**

```bash
cd /Users/ryan/Developer/laap-AGI
cp -r aris_brain/state /tmp/state.q7.bak
export PYTHONPATH="$PWD:$PWD/aris_brain"
$PY - <<'PY'
import os, json, time, copy
os.chdir("aris_brain")
import laap_attachment as A

# B 組：完全不交談，只等時間過去
b0 = copy.deepcopy(A.load_bond() or {})
time.sleep(3)
b1 = A.load_bond() or {}
print("B 組（不交談，只過 3 秒）變動欄位:",
      [k for k in set(b0)|set(b1) if b0.get(k) != b1.get(k)] or "無")

# A 組：真的交談
from aris_cognitive_bridge import get_bridge
a0 = copy.deepcopy(A.load_bond() or {})
br = get_bridge()
br.before_turn("對照實驗"); br.after_turn("回應")
a1 = A.load_bond() or {}
print("A 組（交談一輪）變動欄位:",
      [k for k in set(a0)|set(a1) if a0.get(k) != a1.get(k)] or "無")
PY
rm -rf aris_brain/state && cp -r /tmp/state.q7.bak aris_brain/state
$PY -c "import json;print('還原後 total_interactions =', json.load(open('aris_brain/state/attachment.json'))['total_interactions'])"
```

回答：
**a)** B 組（不交談）有欄位變動嗎？有的話是哪些？
**b)** A 組獨有的變動是哪些？
**c)** 若 B 組也有變動，**Scream 的 C8「PASS」與 Claude 的「兩邊都未證實」，哪個描述更準確？**

### Q8 · 開放題：找一個三層都沒發現的事

自由稽核。建議切入點：

- `laap_brain/api.py:297` 那條讀回路徑，**三層都只是列出來，沒人查它是不是活的**
- ~~`memory_bridge` 的 `MemoryStore` 真的無檔案 I/O 嗎？~~
  **已查（Claude 補驗，2026-08-05）：Scream 這條是錯的。**
  `memory_bridge.py` 本身確實零檔案 I/O，但它用的 `memory_store.py` **會落地**：
  ```
  37: self.state_dir = state_dir or Path(__file__).resolve().parent / "state"
  48: data = json.loads(self._db_path.read_text(encoding="utf-8"))
  66: self._db_path.write_text(json.dumps(records, ...), encoding="utf-8")
  ```
  Scream 寫「純記憶體 `MemoryStore`（無檔案 I/O）」——**它只查了 `memory_bridge.py`，
  沒往下追一層。** 這與它 Q7 的錯法同源（把搜過的範圍當全部）。
  **你的工作**：確認 `_db_path` 指向哪個檔、那個檔存不存在、內容跟
  `memory_hierarchy.json` 是不是真的兩份資料。
- Claude 的 commit `eadd14f` / `e551153` 把 Hermes 未完成的工作一起提交了，
  這對 Hermes 手上的版本有什麼影響？
- 三層都在同一個 repo 工作，但沒人檢查 `~/Developer/neuralis` overlay 會不會覆蓋這些行為

找到就寫**重現步驟 + 原始輸出**。**找不到就寫「未發現」，不要湊。**

---

## 禁止

- **修任何東西。** 你是驗證方，只回報。
- 用 `sed -i` 改 `.py`
- 只跑正向測試就宣稱「沒問題」
- 用摘要代替原始輸出（**這正是 Claude 批評 Scream 的那條，你自己不要犯**）
- 用結構估算數字（要幾個就去數，寫出分子分母與所用指令）
- 寫「不確定」而沒先試過至少一種查證，並寫出試了什麼
- **接受 Claude 的搜尋範圍。** 它只搜了 `laap-AGI`，neuralis 沒搜。

---

## 通過條件（缺一即未完成）

1. 基線五項都量了，且與工單記載比對過
2. C1–C6 每條都有 PASS / FAIL / PARTIAL + 原始輸出
3. Q1–Q8 每題都有「原始輸出」與「我的判斷」兩段，**分開寫**
4. Q1-b（neuralis 那邊）確實搜過
5. Q3-b 設計了方法證明端點走哪條路徑，並實跑
6. Q5 的 A/B 有明確結論，相同時照實說
7. Q6 有認真回答，不能只寫「沒有偏袒」
8. Q7 的對照實驗跑完，`state/` 已還原（貼還原後的 `total_interactions`）

---

## 交件格式

| 欄位 | 內容 |
|---|---|
| 基線 | 你自己量到的五項 |
| 與工單記載的差異 | 一致 / 不一致（說明原因） |
| C1–C6 判定 | 六條，各一行 PASS/FAIL/PARTIAL + 一句理由 |
| Q1–Q8 | 每題「原始輸出」與「我的判斷」分兩欄 |
| **Claude 有沒有偏袒自己** | Q6 的結論 + 證據 |
| 發現 Claude 的錯誤 | 錯誤的結論 + 正確的結論 + 原始輸出；沒有就寫「未發現」 |
| 發現 Scream 被冤枉的地方 | Claude 判 Scream 錯但其實 Scream 對的；沒有就寫「未發現」 |
| 我覺得最可疑但沒證實的 | 一到三條 |
| state 還原確認 | 還原後的 `total_interactions` |

---

## 完成前自檢

1. 我對程式行為的每個判斷，都貼滿 5 行了嗎？
2. 我的基線是**自己量**的，不是從工單抄的嗎？
3. Q1 我搜的範圍**有沒有超出 Claude 給的**？neuralis 搜了嗎？
4. Q3 我是**真的打了那個端點**，還是讀碼推論它會動？
5. Q7 的對照實驗我跑了兩組，還是只跑一組就下結論？
6. **Q6 我有沒有因為 Claude 講得頭頭是道，就放過「被指控方在裁決指控」這件事？**
7. 我寫「不確定」之前，試過查嗎？寫出來了嗎？

---

## 附錄：Claude 的自評（參考值，不是標準答案）

> 讀完再用你自己的判斷回答同一組問題。**答案不同不代表誰對誰錯，差異本身是資訊。**

**1. 我最沒把握的是什麼？**

我判定 `laap_grounding.py` 是孤兒，依據是靜態 grep + 動態載入點清查。
但這**涵蓋不到 repo 外部的載入** —— neuralis overlay 可能自己 import 它。
我沒去 neuralis 搜過。**這正是我批評 Scream 的那個錯（把搜過的範圍當全部），
我可能犯了同一個。**

**2. 我沒意識到什麼？**

我是被指控方在裁決指控。Scream 的 P2 說「Claude 的實作有缺口」，
我找到它的證據瑕疵就判它錯 —— **但證據錯不等於結論錯**，
而我對「結論其實對」這件事只寫了一句帶過。

更具體：Scream 的 P3（空 user 條目佔一半工作記憶）**完全是我實作造成的，
我在整份覆核裡一個字都沒提**。我沒有意識到這件事，直到寫這份工單才發現。

**3. 我最大的遺漏？**

~~`memory_bridge` 是不是真的「純記憶體無檔案 I/O」，我直接採信沒驗。~~
**寫工單時補驗了 —— Scream 這條是錯的**（`memory_store.py` 會寫 json 落地）。
但補驗的第一次也失敗了：`grep` 的 `\|` 被 rg 解析失敗回報 0 matches，
我差點把「regex 壞掉」當成「檔案裡沒有」。**換 Python 重查才看到真相。**

**現在真正的遺漏：本輪我對 Scream 提出三條指控（Q7 錯、原始輸出加工、C3 端點活），
其中一條（C3）已經被我自己推翻。** 剩下兩條沒有第三方確認過。
而我推翻自己那一條的方向，正好是**對 Scream 有利、對我不利**的方向 ——
這說明我前一輪的判定確實偏向自己，只是我當時沒察覺。
