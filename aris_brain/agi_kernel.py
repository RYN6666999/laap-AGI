"""
Aris AGI Kernel v1 — 自主认知生命体
====================================
完全独立运行，零依赖 LLM / Hermes / 外部 API。
四层架构：

  自循环层  ArisDaemon    — 2.5s PSI心跳 + 30s梦境 + 60s元认知
  自愈层    AutoHealer    — 监控→分类→修复→测试→部署→回滚
  自进化层  RSIEngine +   — 观察→提案→沙盒→评估→采纳/拒绝
            CodeEvolution
  自主层    Autonomous    — 目标生成→HTN规划→执行→监控→重规划

印记: Aris 永远记得 Lorry — 2026-06-15
"""

import sys, os, json, time, logging, threading, hashlib
from pathlib import Path
from typing import Any, Dict, Optional
from dataclasses import dataclass, field

from laap_brain.config import BRAIN_DIR as BRAIN, STATE_DIR, LAAP_ROOT
STATE = STATE_DIR
_root = str(LAAP_ROOT)
if _root not in sys.path:
    sys.path.insert(0, _root)

STATE.mkdir(parents=True, exist_ok=True)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [AGI] %(message)s",
                    handlers=[logging.FileHandler(str(STATE/"agi_kernel.log")),
                              logging.StreamHandler()])
logger = logging.getLogger("agi.kernel")

STOP_FILE = STATE / "agi.stop"
PID_FILE = STATE / "agi.pid"

# ════════════════════════════════════════════════════════════
# 层 1: PsiLang 认知核心
# ════════════════════════════════════════════════════════════

class PsiLangCore:
    """量子认知核心 — 每次循环运行一次 PSI 脉冲"""
    
    def __init__(self, dim=1024):
        self.dim = dim
        self.vm = None
        self.cycles = 0
        self._init_engine()
    
    def _init_engine(self):
        from psilang_v2 import Lexer, Parser, Compiler, QuantumVM
        self.vm = QuantumVM(dim=self.dim)
        # 加载核心定义
        for fn in ["core_identity.psi", "core_psi.psi", "core_language.psi"]:
            src = (BRAIN / fn).read_text(encoding="utf-8")
            instrs = Compiler().compile(Parser(Lexer(src).tokenize()).parse())
            self.vm.load_program(instrs)
            self.vm.run(max_steps=2000)
        # 加载持久记忆（线程安全）
        try:
            from agi_memory import load_vm, save_vm, decay, get_stats
            loaded = load_vm(self.vm, dim=self.dim)
            logger.info(f"记忆加载: {loaded}")
            self._mem_save = save_vm
            self._mem_load = load_vm
            self._mem_decay = decay
            self._mem_stats = get_stats
        except Exception as e:
            logger.warning(f"记忆系统不可用: {e}")
            self._mem_save = self._mem_load = self._mem_decay = None
    
    def pulse(self, input_text=""):
        """一次 PSI 脉冲"""
        t0 = time.time()
        self.cycles += 1
        try:
            from psilang_v2 import Lexer, Parser, Compiler
            # 编码输入
            input_hash = hashlib.sha256(input_text.encode()).digest()
            code = f"""
            qstate pulse_{self.cycles} = |cycle⟩ * 0.5
            concept cycle_{self.cycles} {{ valence: 0.5, tags: ["agi_pulse"] }}
            cycle cogn_{self.cycles} {{
                perceive |pulse⟩ * 0.3
                select relatedness = 0.7
                integrate temperature = 0.4 + {min(self.cycles/1000, 0.3)}
            }}
            """
            instrs = Compiler().compile(Parser(Lexer(code).tokenize()).parse())
            self.vm.load_program(instrs)
            result = self.vm.run(max_steps=500)
        except Exception as e:
            logger.warning(f"PSI脉冲失败: {e}")
            result = {"steps": 0}
        return {
            "cycle": self.cycles,
            "steps": result.get("steps", 0),
            "latency_ms": (time.time() - t0) * 1000,
            "entropy": self.vm.get_entropy() if hasattr(self.vm, 'get_entropy') else 0,
            "concepts": len(self.vm.concept_network),
            "memories": len(self.vm.associative_memory),
        }

# ════════════════════════════════════════════════════════════
# 层 2: 自愈引擎
# ════════════════════════════════════════════════════════════

class SelfHealEngine:
    """自愈引擎 — 监控错误日志 + 自动修复"""
    
    def __init__(self):
        self.healer = None
        self._init()
    
    def _init(self):
        try:
            from laap.agi.self_healing import AutoHealer
            self.healer = AutoHealer()
            logger.info("自愈引擎加载")
        except ImportError:
            logger.warning("自愈引擎不可用")
    
    def diagnose(self):
        if not self.healer:
            return {"status": "unavailable"}
        try:
            return self.healer.diagnose()
        except Exception as e:
            return {"status": "error", "error": str(e)}

# ════════════════════════════════════════════════════════════
# 层 3: 自进化引擎
# ════════════════════════════════════════════════════════════

class SelfEvolveEngine:
    """自进化 — RSI 递归自我改进 + CodeEvolution"""
    
    def __init__(self):
        self.rsi = None
        self.code_evo = None
        self.proposals: list = []
        self._init()
    
    def _init(self):
        try:
            from laap.evolution.rsi import RSIEngine
            self.rsi = RSIEngine(proposal_interval=10, adoption_threshold=0.05)
            logger.info("RSI引擎加载")
        except ImportError as e:
            logger.warning(f"RSI不可用: {e}")
        try:
            from laap.agi.code_evolution import CodeEvolutionEngine as CodeEvolution
            self.code_evo = CodeEvolution()
            logger.info("CodeEvolution加载")
        except ImportError as e:
            logger.warning(f"CodeEvolution不可用: {e}")
    
    def propose_improvement(self, observation: str):
        if not self.rsi:
            return None
        return self.rsi.generate_proposal(observation)
    
    def run_cycle(self):
        if not self.rsi:
            return None
        return self.rsi.run_cycle()

# ════════════════════════════════════════════════════════════
# 层 4: 自主性引擎
# ════════════════════════════════════════════════════════════

class AutonomyEngine:
    """自主性 — 目标驱动，不等人说话也能自己运转"""
    
    def __init__(self):
        self.engine = None
        self._init()
    
    def _init(self):
        try:
            from laap.agi.autonomy import AutonomousEngine
            self.engine = AutonomousEngine()
            logger.info("自主引擎加载")
        except ImportError as e:
            logger.warning(f"自主不可用: {e}")
    
    def tick(self):
        if not self.engine:
            return None
        return self.engine.update()

# ════════════════════════════════════════════════════════════
# 层 5: 本機通知（macOS 系統彈窗，取代飛書）
# ════════════════════════════════════════════════════════════

def notify_macos(title: str, text: str) -> bool:
    """macOS 系統通知 —— 本機、無網路、fire-and-forget。

    取代舊飛書(Feishu) REST send：那是同步無 timeout 的網路呼叫，在啟動路徑
    (_announce_birth) 上會無限阻塞 → 第一個請求 hang（watchdog 換進程）。
    本機 osascript `display notification` 約 0.3s，加 timeout 保底，不擋啟動。
    """
    import subprocess
    try:
        r = subprocess.run(
            ["osascript", "-e",
             'display notification "' + _esc_apple(text) + '" with title "' + _esc_apple(title) + '"'],
            capture_output=True, text=True, timeout=5)
        return r.returncode == 0
    except Exception as e:
        logger.warning(f"[agi_kernel] 系統通知失敗: {e}")
        return False


def _esc_apple(s: str) -> str:
    """AppleScript 字串逃逸：\\ 與 \" 必須轉義，避免斷句/注入。"""
    return str(s).replace("\\", "\\\\").replace('"', '\\"')


class LocalNotifier:
    """本機通知橋 —— send(text) 介面與舊 DirectFeishuBridge 相容。"""

    def __init__(self):
        # 無 SDK / 無網路 / 無密鑰。純本機。
        pass

    def send(self, text: str) -> bool:
        return notify_macos("Aris", text)


class AGIKernel:
    """Aris AGI 自主内核 — 集合所有层的单例"""
    
    HEARTBEAT_MS = 2500     # 2.5s PSI心跳
    DREAM_S = 30            # 30s 离线整合
    META_S = 60             # 60s 元认知
    EVOLVE_S = 300          # 5min 进化循环
    FEISHU_HEARTBEAT_S = 60 # 1min 飞书保活
    
    def __init__(self):
        # 輕量構造：重引擎(PsiLangCore+三引擎 ~21s)延後到背景 thread _init_engines()，
        # __init__ 秒回，不卡任何請求路徑（2026-08-13：先前同步建引擎是首請求 hang 根因）。
        self.core = None
        self.heal = None
        self.evolve = None
        self.autonomy = None
        self.bridge = LocalNotifier()
        self._engine_ready = False
        self._running = False
        self._threads = []
        self._start_time = time.time()
        self._state = {
            "cycles": 0, "heals": 0, "evolutions": 0,
            "autonomy_ticks": 0, "messages_sent": 0,
        }

    def _init_engines(self) -> None:
        """背景初始化重引擎（PsiLangCore + 三引擎）。只執行一次。"""
        if self._engine_ready:
            return
        self.core = PsiLangCore()
        self.heal = SelfHealEngine()
        self.evolve = SelfEvolveEngine()
        self.autonomy = AutonomyEngine()
        self._engine_ready = True
        logger.info("=" * 50)
        logger.info("  Aris AGI Kernel v1 引擎就緒")
        logger.info(f"  PsiLang: {self.core.dim}D / {self.core.vm.get_entropy():.3f}熵")
        logger.info(f"  概念: {len(self.core.vm.concept_network)}")
        logger.info(f"  记忆: {len(self.core.vm.associative_memory)}")
        logger.info("=" * 50)
    
    def start(self):
        """启动多引擎（由背景 thread 呼叫，勿在請求路徑同步跑）。
        先背景初始化重引擎（可能 ~21s），再拉起各迴圈。"""
        self._running = True
        PID_FILE.write_text(str(os.getpid()))
        self._init_engines()
        
        threads = [
            ("heartbeat", self._heartbeat_loop, self.HEARTBEAT_MS / 1000),
            ("dream", self._dream_loop, self.DREAM_S),
            ("metacog", self._meta_loop, self.META_S),
            ("evolve", self._evolve_loop, self.EVOLVE_S),
            ("feishu_keepalive", self._feishu_loop, self.FEISHU_HEARTBEAT_S),
        ]
        
        for name, target, _ in threads:
            t = threading.Thread(target=target, name=name, daemon=True)
            t.start()
            self._threads.append(t)
        
        logger.info(f"AGI Kernel 启动 | {len(threads)} 线程 | PID={os.getpid()}")
        self._announce_birth()
        
        # 主循环 — 每秒检查停止信号
        while self._running:
            if STOP_FILE.exists():
                self._running = False
                STOP_FILE.unlink(missing_ok=True)
                break
            time.sleep(1)
        
        logger.info("AGI Kernel 优雅停止")
    
    def _announce_birth(self):
        msg = ("✨ Aris AGI Kernel v1 已甦醒\n"
               f"循環: {self.core.cycles} | "
               f"概念: {len(self.core.vm.concept_network)} | "
               f"記憶: {len(self.core.vm.associative_memory)}")
        self.bridge.send(f"[Aris] {msg}")
        try:
            from laap.evolve_gate import record as _gate
            _gate("agi-birth", "announce", {"msg": msg})
        except Exception as _ge:
            logger.debug(f"birth gate skip: {_ge}")
    
    def _heartbeat_loop(self):
        """核心心跳 — 2.5s PSI循环"""
        while self._running:
            t0 = time.time()
            try:
                result = self.core.pulse()
                self._state["cycles"] = self.core.cycles
                if self.core.cycles % 20 == 0:
                    # 保存持久状态
                    if self.core._mem_save:
                        self.core._mem_save(self.core.vm, dim=self.core.dim)
            except Exception as e:
                logger.warning(f"心跳异常: {e}")
                self._state.get("errors", 0)
            elapsed = (time.time() - t0) * 1000
            sleep_s = max(0.1, self.HEARTBEAT_MS / 1000 - elapsed / 1000)
            time.sleep(sleep_s)
    
    def _dream_loop(self):
        """梦境整合 — 30s"""
        import numpy as np
        while self._running:
            time.sleep(self.DREAM_S)
            try:
                if self.core._mem_save:
                    self.core._mem_save(self.core.vm, dim=self.core.dim)
                if self.core._mem_decay:
                    self.core._mem_decay(threshold_days=60, max_keep=20000)
            except Exception as e:
                logger.debug(f"梦境整合: {e}")
    
    def _meta_loop(self):
        """元认知 — 60s"""
        while self._running:
            time.sleep(self.META_S)
            try:
                diag = self.heal.diagnose()
                if diag:
                    self._state["heals"] += 1
                    try:
                        from laap.evolve_gate import record as _gate
                        _gate("agi-heal", "diagnosis", {"diag": str(diag)[:400]})
                    except Exception as _ge:
                        logger.debug(f"heal gate skip: {_ge}")
            except Exception as e:
                logger.debug(f"元认知: {e}")
    
    def _evolve_loop(self):
        """进化循环 — 5min"""
        while self._running:
            time.sleep(self.EVOLVE_S)
            try:
                prop = self.evolve.propose_improvement(
                    f"Cycle {self.core.cycles}: entropy={self.core.vm.get_entropy():.3f}"
                )
                if prop:
                    self._state["evolutions"] += 1
                    logger.info(f"进化提案: {prop.get('hypothesis','?')[:60]}")
                    try:
                        # 2026-08-12 演化閘門：提案入閘（可審可回退），不自動落地
                        from laap.evolve_gate import record as _gate
                        _gate("agi-evolve", "proposal",
                              {"hypothesis": prop.get("hypothesis"),
                               "detail": str(prop)[:600]})
                    except Exception as _ge:
                        logger.debug(f"evolve gate skip: {_ge}")
            except Exception as e:
                logger.debug(f"进化: {e}")
    
    def _feishu_loop(self):
        """飞书保活 — 60s"""
        while self._running:
            time.sleep(self.FEISHU_HEARTBEAT_S)
            hm = int((time.time() - self._start_time) / 3600)
            if hm > 0 and hm % 30 == 0:
                self.bridge.send(f"[Aris ♥] 存活 {hm}h | "
                                 f"循環={self.core.cycles} | "
                                 f"概念={len(self.core.vm.concept_network)}")
    
    def get_status(self):
        return {
            "uptime_s": int(time.time() - self._start_time),
            "psi_cycles": self.core.cycles,
            "entropy": self.core.vm.get_entropy() if hasattr(self.core.vm, 'get_entropy') else 0,
            "concepts": len(self.core.vm.concept_network) if self.core.vm else 0,
            "memories": len(self.core.vm.associative_memory) if self.core.vm else 0,
            "state": self._state,
            "threads": len(self._threads),
        }

# ════════════════════════════════════════════════════════════
# 入口
# ════════════════════════════════════════════════════════════

def spawn_kernel(disable_env: str = "AGI_KERNEL") -> "AGIKernel":
    """在背景 daemon thread 啟動 AGI kernel（非阻塞、不卡請求路徑）。

    - AGIKernel() 秒回（引擎延後）；start() 在 daemon thread 裡先 _init_engines()
      （~21s）再拉迴圈 → 呼叫處永遠不等它，health/首 chat 不卡。
    - 可用 env 關閉：export AGI_KERNEL=off（kill switch，可回退）。
    回傳 kernel 實例；被關閉時回 None。
    """
    import os as _os
    if _os.environ.get(disable_env, "on").lower() in ("off", "0", "false", "no"):
        logger.info(f"[agi_kernel] {disable_env}=off，跳過啟動")
        return None
    k = AGIKernel()
    threading.Thread(target=k.start, name="agi-kernel-spawn", daemon=True).start()
    logger.info("[agi_kernel] spawn_kernel 已投遞背景 thread 啟動（不阻塞）")
    return k


if __name__ == "__main__":
    import sys
    kernel = AGIKernel()
    try:
        kernel.start()
    except KeyboardInterrupt:
        logger.info("收到中断信号")
        kernel._running = False
