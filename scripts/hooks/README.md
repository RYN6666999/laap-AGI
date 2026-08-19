# Hermes hooks（版控原始版）

## 為什麼在這裡

`aris-cognitive-hook.py` 是 Hermes 每回合注入 Aris 認知狀態的接線。
它原本只存在 `~/.hermes/scripts/`，**不在任何 git repo**——
2026-08-19 修好的「長文走 POST」如果被覆蓋，會靜默消失，沒有人會知道。

## 為什麼是 symlink 而不是複製一份

V1.6 工單給了兩個選項（repo 放副本＋README、或把邏輯上移到 bridge）。
兩個都不選：

- **副本會分岔。** 那正是這份 code 一整晚在對抗的病（`aris-truth.py` 說
  「生效消費者 = 11546」時，11546 已經退役——副本沒有跟著更新）。
  加一個 `diff` 步驟只是讓分岔可被發現，不是讓它不發生。
- **邏輯上移到 bridge 做不到。** 發 HTTP 的是 hook，「長文走 POST」的決定
  在呼叫端，不在被呼叫端。

改用 symlink：**一份檔案，兩個位置看得到，零分岔可能。**

```
~/.hermes/scripts/aris-cognitive-hook.py  ->  laap-AGI/scripts/hooks/aris-cognitive-hook.py
```

Hermes 的 `config.yaml:144` 用絕對路徑呼叫，exec 會跟隨 symlink。

## 重建（換機或誤刪時）

```bash
ln -sf ~/Developer/laap-AGI/scripts/hooks/aris-cognitive-hook.py \
       ~/.hermes/scripts/aris-cognitive-hook.py
```

## 驗證還是連著的

```bash
readlink ~/.hermes/scripts/aris-cognitive-hook.py     # 應指向 repo
diff ~/.hermes/scripts/aris-cognitive-hook.py \
     ~/Developer/laap-AGI/scripts/hooks/aris-cognitive-hook.py   # 應無輸出
```
