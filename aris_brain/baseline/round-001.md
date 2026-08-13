# Aris 育種基線記錄 — 第 1 輪 (2026-08-06)

## 狀態：什麼都沒改

## 工具呼叫總覽（最近 100 筆 from Hermes DB）

**整體一次成功率：82/100 = 82.0%**

| 工具 | 次數 | 成功 | 成功率 | 類別 |
|---|---|---|---|---|
| terminal | 52 | 43 | 83% | 主測 |
| read_file | 15 | 13 | 87% | 主測 |
| browser_navigate | 6 | 4 | 67% | 主測 |
| search_files | 4 | 4 | 100% | 主測 |
| skill_view | 4 | 1 | 25% | 主測 |
| mcp__aris__aris_cognitive | 3 | 3 | 100% | 主測 |
| todo | 3 | 3 | 100% | 主測 |
| session_search | 3 | 1 | 33% | 主測 |
| execute_code | 1 | 1 | 100% | 主測 |
| skills_list | 1 | 1 | 100% | 主測 |
| browser_scroll | 1 | 1 | 100% | 主測 |
| clarify | 1 | 1 | 100% | 主測 |
| gbrain (mcp) | 2 | 2 | 100% | ⭐ 控制 |
| write_file | 1 | 1 | 100% | 主測 |
| tool_describe | 1 | 1 | 100% | 主測 |
| memory | 1 | 1 | 100% | 主測 |
| patch | 1 | 1 | 100% | 主測 |

## 對照工具選定

**gbrain MCP 工具組（mcp__gbrain__search, mcp__gbrain__list_pages）** 當控制。
原因：
- 與 terminal / read_file / browser 等 Hermes 核心工具架構隔離
- 如果改記憶檢索邏輯，gbrain 讀取不該受影響
- 如果 terminal 成功率變了但 gbrain 沒變 → 改動有效
- 如果兩個都變了 → 環境問題，不是改動

## 失敗分析（18 次失敗）

terminal 失敗 9 次：
- 「exit_code: 1」類型 — 命令本身回傳非零
- 無 timeout 或 infrastructure 錯誤

read_file 失敗 2 次：
- 檔案不存在（路徑錯誤或暫存檔已刪除）

browser_navigate 失敗 2 次：
- 1 次 bot detection（Brave/Captcha）
- 1 次 DNS 解析失敗

skill_view 失敗 3 次：
- 1 次 skill 不存在
- 2 次待確認（內容含 error 模式）

session_search 失敗 2 次：
- 可能是 query 格式問題

## 可預測性評估

下一輪一次成功率預測：**80-84%**
依據：
- 最近 100 筆 = 82%
- terminal 穩定在 83% 附近
- 失敗主要是環境問題（bot detection、檔案不存在）而非工具本身
- 預測區間基於 100 筆樣本 ±2%

## 記錄格式 (outcome schema)

```json
{
  "generation": null,
  "round": 1,
  "timestamp": "2026-08-06",
  "changed_anything": false,
  "tool_calls_sampled": 100,
  "overall_success_rate": 0.82,
  "control_success_rate": 1.0,
  "control_tool": "gbrain MCP",
  "by_tool": { ... },
  "failure_breakdown": "詳見上文",
  "prediction_next": "80-84%"
}
```

## 待辦

- [ ] 第 2 輪基線（再累積 100 筆工具呼叫，不改變任何東西）
- [ ] 驗證預測：下一輪是否落在 80-84% 內