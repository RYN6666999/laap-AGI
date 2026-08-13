# 稽核報告：`aris_cognitive_bridge.py` 分層記憶掛鉤

**稽核方：** Scream Code（獨立稽核）  
**日期：** 2026-08-05  
**受稽核方：** Claude Code

---

## 基線

| 項目 | 量測值 | 工單記載 | 比對 |
|------|--------|---------|------|
| SHA | `f249dbf4c18d60d60ff3639349700bd003abffd9` | `f249dbf4…` | ✅ 一致 |
| 行數 | 1667 (Python) / 1666 (wc -l) | 1667 | ✅ 一致（wc -l 與 split("\n") 差 1 為標準 off-by-one） |
| `memory_hierarchy.json` | 不存在 | 不存在 | ✅ 一致 |
| `total_interactions` | 4 | 4 | ✅ 一致 |

---

## 取樣範圍

實際貼了以下行數（原始 sed/awk 輸出均附於各題）：
- Import 區塊：33–45
- Helper 定義：526–545
- before_turn：546–706
- Helper 呼叫點：560–578
- LIGHT 分支：570
- 統計注入點：594–610
- after_turn：707–735
- `laap_memory_hierarchy.py` 結構：44–66
- `_classify_load`：1455–1475
- `_forget` / `_consolidate` / `recall`：全函數

**擴大範圍：** 讀了 `laap_memory_hierarchy.py` 完整常數段（1–43 行）、`memory_bridge.py` 全文（67 行）、`_extract_facts` 實作、`add_to_memory` 完整實作。工單給的範圍涵蓋了關鍵路徑，但為確認 Q7/Q8 有必要擴大。

---

## C1–C8 判定

| 編號 | 宣稱 | 判定 | 理由 |
|------|------|------|------|
| C1 | 只新增，沒刪改任何原有邏輯 | **PASS** | diff 結果：6 hunk、51 新增、**0 刪除**。符合工單記載。 |
| C2 | import 區塊有防護，模組缺失不會炸 | **PASS** | try/except Exception 包裹，缺失時 `_mem_hier = None`、`_mem_hier_available = False`。 |
| C3 | helper 失敗時回空字串、不拋例外 | **PASS** | 兩個防護點：`if not _mem_hier_available: return ""` 和 `except Exception: return ""`。 |
| C4 | helper 的呼叫點在 LIGHT 分支之前 | **PASS** | 第 567 行呼叫 `_record_and_summarize_memory`，第 570 行才檢查 LIGHT 分支。 |
| C5 | 統計文字有注入 cognitive_context | **PASS** | 第 599–601 行：`if memory_note: context_parts.append(memory_note)`。 |
| C6 | after_turn 有寫入回應並更新依戀 | **PASS** | 第 717–722 行：`add_to_memory("", response)` + `_update_bond(...)`，try/except 包裹。 |
| C7 | dict 層級正確 | **PASS** | `mem.get("stats").get("total_messages")` 與 `laap_memory_hierarchy.py` 第 16–21 行結構一致。`or {}` 防護處理了 None 與空 dict。 |
| C8 | 依戀值真的有變動 | **PASS** | 實測 3 輪對話：`bond_level` 16.75→17.875、`familiarity` 0.0535→0.05575、`attachment` 0.12057→0.12096、`total_interactions` 4→7。 |

---

## Q1–Q9

### Q1 · `before_turn` 有幾個 return 出口？

**原始輸出：**
```
565:         # 必须在 LIGHT 分支之前：_light_turn 是另一个 return 出口，
571:             return self._light_turn(user_message)
687:             return {  ← 完整 FULL 模式回傳 (含 cognitive_context、focus、emotion 等)
```

**我的判斷：**  
2 個 return 出口。  
- **第 571 行**：LIGHT 模式（`return self._light_turn(user_message)`）  
- **第 687–706 行**：FULL 模式（return dict）  

記憶寫入（`_record_and_summarize_memory`）在第 567 行，**兩條路徑之前**，所以兩種模式都不會漏掉。✓

---

### Q2 · `self._last_user_message` 在檔案裡被設定了幾次？

**原始輸出：**
```
529:        _last_user_message 在这里也设一次：原本只在 _perceive 里设，
532:        self._last_user_message = user_message   ← 在 _record_and_summarize_memory 中
726:                _update_bond(getattr(self, "_last_user_message", "") or "")  ← 讀取
946:        self._last_user_message = user_message   ← 在 _perceive 中
1272:            current_topics = getattr(self, '_last_user_message', response)  ← 讀取
```

**設定點（2 次）：**
1. **第 532 行**：`_record_and_summarize_memory` → 從 `before_turn` 呼叫，**兩條路徑都走**
2. **第 946 行**：`_perceive` → 從 `before_turn` 的 FULL 路徑呼叫

**讀取點（2 次）：**
1. **第 726 行**：`after_turn` 中更新依戀時讀取
2. **第 1272 行**：`_detect_topics` 中讀取

**我的判斷：**  
FULL 模式下，第 532 行先設 `user_message`，然後第 946 行再設一次（同一個值）。`after_turn` 讀到的是第 946 行設的值（因為 `_perceive` 後執行）。  
LIGHT 模式下，`_perceive` 不執行，所以 `after_turn` 讀到的是第 532 行設的值。**兩種模式下值相同（都是 `user_message`）。** ✓

---

### Q3 · `_load_memory_context()` 被呼叫了幾次？

**原始輸出：**
```
594:        integrated = integration + "\n" + self._load_memory_context()
1236:    def _load_memory_context(self) -> str:
1586:            ctx = self._integrate() + "\n" + self._load_memory_context()
```

**我的判斷：**  
2 次呼叫（不含定義行 1236）：
1. **第 594 行**：在 `before_turn` 的 FULL 路徑中（`_integrate()` 之後）
2. **第 1586 行**：在 `get_context()` 方法中（fallback 路徑，當 `_last_context` 為 None 時）

兩次都屬於 `CognitiveBridge` 類別的方法。

---

### Q4 · 一輪對話，`total_messages` 會加幾？

**原始輸出：**
```
聊了 3 輪
total_messages = 6
working_memory 條數 = 6
user 欄位為空的條數 = 3

--- working_memory 內容 ---
  [0] user='第 1 句話' assistant=''
  [1] user='' assistant=''
  [2] user='第 2 句話' assistant=''
  [3] user='' assistant=''
  [4] user='第 3 句話' assistant=''
  [5] user='' assistant=''
```

**我的判斷：**  
- 聊 3 輪 → `total_messages = 6`  
- 每輪加 **2**（`before_turn` 寫入 user + `after_turn` 寫入 assistant 回應）  
- 注入文字「X 次对话历历在目」：X = `total_messages` = **真實輪數 × 2**  
- `user` 為空的條目 = 3/6 = **1/2**（全部來自 `after_turn` 的 `add_to_memory("", response)` 呼叫）  

`_extract_facts` 只對 `user_msg` 做關鍵字匹配（`r"(?:我|我们)..."`），空字串不匹配任何 pattern → 不產生事實。所以空 user 條目在 `_extract_facts` 眼中相當於無害的填充物，**不產生錯誤但浪費工作記憶槽位**。

---

### Q5 · LIGHT 模式現在會不會被觸發？

**原始輸出：**
```
_router_available = False
full   <- ls
full   <- hi
full   <- 修一下 bug
full   <- 跑測試
full   <- 你好嗎
```

**我的判斷：**  
**LIGHT 模式是死的。** `_router_available = False` 導致 `_classify_load` 始終回傳 `"full"`。LIGHT 分支從未被觸發。

被稽核方為它寫的防護（`_record_and_summarize_memory` 放在 LIGHT 分支之前）是**負責任的預防性設計**——如果未來 `_router_available` 變成 True，記憶掛鉤不會因為 LIGHT 分支早退而漏掉。但以現狀來說，這是**超前防護**，不是必要修復。

---

### Q6 · A/B 反向測試 — 這次修改到底有沒有作用？

**原始輸出：**
```
A 組 before_turn(強制LIGHT): 0 -> 1  delta=1
B 組 _light_turn 直呼      : 1 -> 1  delta=0
```

**我的判斷：**  
**A 組 +1，B 組 +0 — 判準通過。**  
- A 組（強制 LIGHT 的 `before_turn`）：記憶被寫入 ✓  
- B 組（直接呼叫 `_light_turn`）：記憶不被寫入 ✓  

但這只證明**強制觸發時會記憶**，**不證明真實使用中 LIGHT 會記憶**——因為真實使用中 LIGHT 從未被觸發（見 Q5）。兩個結論不衝突：修改正確，但對當前使用者無效，因為觸發條件不存在。

---

### Q7 · 兩套記憶系統是不是在各寫各的？

**原始輸出：**
```
=== memory_bridge.py ===
（無 STATE_DIR / .json 寫入 — 純 MemoryStore 記憶體）

=== laap_memory_hierarchy.py ===
35:STATE_DIR = BRAIN / "state"
70:    path = STATE_DIR / "memory_hierarchy.json"
80:    STATE_DIR.mkdir(exist_ok=True)
81:    path = STATE_DIR / "memory_hierarchy.json"

=== get_memory_context ===
memory_bridge.py:24:def get_memory_context(...)
```

**我的判斷：**  

1. **兩者寫的是不同檔案/不同資料**  
   - `memory_bridge.py` → 純記憶體 `MemoryStore`（無檔案 I/O）  
   - `laap_memory_hierarchy.py` → `state/memory_hierarchy.json`  

2. **`before_turn` 注入給 LLM 的上下文走的是哪一套？**  
   - 詳細記憶上下文：走 `memory_bridge.get_memory_context()`（第 594 行 `_load_memory_context()`）  
   - 統計摘要：走 `laap_memory_hierarchy` 的 `add_to_memory` 回傳值（第 599–601 行 `memory_note`）  
   - **兩套都有注入，但詳細內容只來自舊系統。**

3. **新掛的這套，寫進去之後有沒有任何地方讀回來？**  
   **沒有。** `laap_memory_hierarchy.py` 有完整的 `recall()` 和 `get_recalled_context()` 函數，但 `aris_cognitive_bridge.py` 從未呼叫它們。新系統是**純寫入**——資料累積在 `memory_hierarchy.json` 但從未被讀回用於 LLM 上下文。  

**結論：兩套系統並存但功能斷裂。新系統寫入的詳細資料沒有任何讀回路徑。**

---

### Q8 · 找一個它沒發現的 bug

**自由稽核範圍：**

**發現 1：`after_turn` 的空 user 條目占 1/2 工作記憶槽位（設計問題，非 Crash）**  
- 每輪產出 2 條工作記憶：1 條有 user（`before_turn`），1 條 user 為空（`after_turn`）  
- 空 user 條目不產生事實、情感權重為 0  
- `_consolidate` 的 `user_msgs` 過濾掉空 user，但 `key_facts` 仍包含它們（`emotional_weight > 0.4` 才會進，而空 user 的權重為 0，所以不會進）  
- `recall` 的 `text = entry.get("user", "") + entry.get("aris", "")` — 空 user 條目的 `aris` 回應仍可被搜尋到  
- **影響：** 工作記憶容量的一半被「無事實」條目佔據。若 `WORKING_MEMORY_MAX = 100`，實際只能容納 50 輪對話的有效記憶才觸發合併。

**發現 2：`_forget` 的 `kept` 變數類型確認（無 Bug，但值得驗證）**  
- 追蹤 `s[2]` 是 `fact` dict 而非 index，`kept` 是 `[fact_dict, ...]` ✓  
- 語意索引重建使用 `enumerate(kept)`，索引正確 ✓  
- 結論：不是 bug，但閱讀時容易誤判，建議加註釋。

**未發現：** 沒有找到會導致 Crash 或資料損毀的 bug。

---

### Q9 · 「我不確定」的使用規則

本稽核未使用「不確定」。所有查證均附原始輸出。

---

## 發現的 bug

**沒有致命的 Crash bug。** 以下為有意義但非致命的問題：

| 嚴重性 | 問題 | 影響 |
|--------|------|------|
| 🟡 P2 | 新記憶系統寫入無讀回路徑（Q7-3） | `memory_hierarchy.json` 累積資料但 LLM 從未讀取詳細內容，只讀統計摘要 |
| 🟡 P2 | LIGHT 模式為死碼（Q5） | `_router_available = False`，LIGHT 分支永不觸發。記憶掛鉤的 LIGHT 防護目前無實際作用 |
| 🟢 P3 | 空 user 條目佔 1/2 工作記憶（Q4/Q8） | 每輪 `after_turn` 產生 1 條無事實條目，浪費槽位但不會造成錯誤 |

---

## 我覺得最可疑但沒證實的

1. **`_forget` 的 `kept` 重建索引** — 語意索引重建時 `enumerate(kept)` 的索引是 0-based，但 `recall` 中 `facts[fid]` 的 `facts` 是否永遠與 `kept` 同步？目前確認同步，但 `_forget` 和 `add_to_memory` 之間若有併發寫入可能有競態。
2. **`add_to_memory` 的 read-modify-write 競態** — 多執行緒下 `load_memory()` → 修改 → `save_memory()` 不是原子操作。但 `aris_cognitive_bridge` 是同步單線程，目前無風險。
3. **`emotional_landmarks` 被 `after_turn` 空 user 條目污染** — 空 user 的 `emotional_weight=0`，不會超過 0.5 閾值，所以不會進 emotional_landmarks。但確認了這件事。

---

## State 還原確認

```
total_interactions restored = 4
```

測試前的 `state/` 目錄已完整還原，`attachment.json` 的 `total_interactions` 回到 4。

---

## 總結

C1–C8 全 PASS。被稽核方正確地將分層記憶掛鉤插入了 `aris_cognitive_bridge.py`，有適當的防護，沒有破壞原有邏輯。兩個主要問題是：(1) 新記憶系統的詳細資料沒有讀回路徑，只寫不讀；(2) LIGHT 模式在當前配置下是死碼。這些都不是 Crash bug，但會讓功能不如預期有效。