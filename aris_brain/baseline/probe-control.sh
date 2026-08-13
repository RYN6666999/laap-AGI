#!/bin/bash
# gbrain 控制組探測 — 給育種基線用的被動資料收集
# 呼叫 gbrain MCP 工具 30 次，不改變任何資料
# 
# 用法: bash probe-control.sh [count=30]

COUNT=${1:-30}
BASELINE_DIR="/Users/ryan/Developer/laap-AGI/aris_brain/baseline"

# 探測查詢列表（唯讀，不修改任何資料）
QUERIES=(
    "taiwan property"
    "laap core"
    "aris memory"
    "brain health"
    "psilang"
    "neuralis"
    "gbrain"
    "psi daemon"
    "attachment"
    "usermodel"
    "hebbian"
    "emotion engine"
    "cognitive bridge"
    "goal engine"
    "rules"
)

echo "[probe-control] 開始探測: $(date)"
echo "[probe-control] 目標: ${COUNT} 次控制組呼叫"
echo "[probe-control] ====="

for i in $(seq 1 $COUNT); do
    q="${QUERIES[$((i % ${#QUERIES[@]}))]}"
    
    # 交替使用 search 和 query 以覆蓋不同 gbrain 端點
    if [ $((i % 2)) -eq 0 ]; then
        # gbrain search
        curl -s --connect-timeout 5 "http://localhost:11546/v1/search?q=${q}" > /dev/null 2>&1
        result=$?
    else
        # gbrain health
        curl -s --connect-timeout 5 "http://localhost:11546/health" > /dev/null 2>&1
        result=$?
    fi
    
    if [ $result -eq 0 ]; then
        echo "  [$i/$COUNT] ✅ ${q}"
    else
        echo "  [$i/$COUNT] ❌ ${q} (exit=$result)"
    fi
    
    # 間隔 200ms 以免被當成 DoS
    sleep 0.2
done

echo "[probe-control] ====="
echo "[probe-control] 完成: $(date)"
echo "[probe-control] 記錄已自動進入 Hermes session DB"
