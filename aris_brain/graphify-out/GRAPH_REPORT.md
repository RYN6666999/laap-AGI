# Graph Report - aris_brain  (2026-08-24)

## Corpus Check
- 94 files · ~140,589 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1986 nodes · 3266 edges · 113 communities (98 shown, 15 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 138 edges (avg confidence: 0.55)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `94b9b58c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- EmotionEngine
- psilang_mini.py
- ChromaMemoryBackend
- laap_usermodel.py
- .generate
- ArisCognitiveBridge
- KnowledgeGrounderV2
- MatrixProductState
- QuantumBasis
- LaapIntegrator
- PsiCognitiveIntegrator
- state_snapshot.py
- DesireEngine
- laap_brain_api.py
- SelfEvolveEngine
- GoalEngine
- QuantumSubconscious
- QuantumCognitiveBridge
- .generate_paper
- RulesEngine
- PsiSemioticsBridge
- StructuredQuantumKernel
- MobileSyncHandler
- aris_goal_engine.py
- SemanticFrame
- Rotor
- BilingualQuantumKernel
- MQTTProxy
- EmbeddingProvider
- psi_core_bridge.py
- PsiSemioticsEngine
- ChineseProseKernel
- SchrodingerEvolution
- PSI-JSpace 植入协议 v1
- EmotionalEngine
- laap_bootstrap.py
- aris_cognitive_bridge.py
- StructuredSemanticEncoder
- SemanticDictEncoder
- Ψ-Semiotics — 量子符号学框架
- aris_fusion_engine.py
- BigramEncoder
- .__init__
- EpisodicMemory
- aris_telemetry.py
- AGISubscriber
- MQTTProxy
- MemoryStore
- governor_integration.py
- psi_semiotics_cli.py
- aris_lm_v5.py
- aris_watchdog.py
- VerificationSuite
- LiushuQuantumKernel
- cognitive_bus.py
- laap_attachment.py
- LongFormSynthesizer
- CognitiveBus
- laap_memory_hierarchy.py
- HebbianLearner
- ao_v10_feishu_bridge.py
- NeedConstitution
- .before_turn
- aris_feishu_bot.py
- aris_messenger.py
- .route
- InternalWorldModel
- Multivector
- AGIKernel
- ConceptGraph
- PhysicalAnalogies
- ._classify
- PreGenerationGovernor
- PSIGovernor
- ao_feishu_service.py
- aris_proxy.py
- MoodState
- psi_downloader.py
- PSI-JSpace Bridge v1
- SelfVerifier
- aris_mcp_server.py
- config.py
- laap_grounding.py
- get_integrator
- aris_emotion_engine.py
- get_engine
- probe-control.sh
- PsiBridge
- handle_express
- Aris 育種基線記錄 — 第 1 輪 (2026-08-06)
- _fetch_detail
- aris_cognitive_api.py
- Aris 育種基線記錄 — 第 2 輪 (2026-08-06)
- ._perceive
- reflection-001.md
- get_engine
- __init__.py
- agi_kernel.py
- MoodSystem
- NeedHierarchy
- JsonMemoryBackend
- TfidfEmbeddingProvider
- memory_store.py
- MirrorNeuronSystem
- NeedState
- SomaticMarkerSystem
- ToolRegistry
- KeywordEmbeddingProvider
- LaapSemanticMemory
- ChineseTokenizer
- laap_semantic_memory.py

## God Nodes (most connected - your core abstractions)
1. `PsiSemioticsEngine` - 48 edges
2. `LaapIntegrator` - 45 edges
3. `MemoryStore` - 43 edges
4. `ArisCognitiveBridge` - 35 edges
5. `CognitiveBus` - 28 edges
6. `MobileSyncHandler` - 26 edges
7. `QuantumSubconscious` - 24 edges
8. `PsiCognitiveIntegrator` - 24 edges
9. `PsiBridge` - 23 edges
10. `Rotor` - 23 edges

## Surprising Connections (you probably didn't know these)
- `DesireType` --uses--> `MemoryStore`  [INFERRED]
  aris_desire_engine.py → memory_store.py
- `LaapIntegrator` --uses--> `PsiLangCore`  [INFERRED]
  laap_integrator.py → agi_kernel.py
- `LaapIntegrator` --uses--> `SelfHealEngine`  [INFERRED]
  laap_integrator.py → agi_kernel.py
- `LaapIntegrator` --uses--> `SelfEvolveEngine`  [INFERRED]
  laap_integrator.py → agi_kernel.py
- `LaapIntegrator` --uses--> `AutonomyEngine`  [INFERRED]
  laap_integrator.py → agi_kernel.py

## Import Cycles
- None detected.

## Communities (113 total, 15 thin omitted)

### Community 1 - "psilang_mini.py"
Cohesion: 0.07
Nodes (32): PsiLangCore, 量子认知核心 — 每次循环运行一次 PSI 脉冲, Amplify, Call, Compiler, Concept, Cycle, Emit (+24 more)

### Community 2 - "ChromaMemoryBackend"
Cohesion: 0.14
Nodes (8): ChromaMemoryBackend, _get_vector_db_backend(), MemoryBackend, ndarray, Path, Abstract backend for semantic memory persistence/retrieval., ChromaDB persistent vector-store backend. Enabled by setting…, Choose vector database backend based on env and availability.

### Community 3 - "laap_usermodel.py"
Cohesion: 0.25
Nodes (13): _default_profile(), _detect_mood(), _detect_style(), _detect_topics(), _detect_values(), _extract_calling_name(), get_preference_summary(), get_profile_summary() (+5 more)

### Community 4 - ".generate"
Cohesion: 0.06
Nodes (23): aris_say(), aris_say_variants(), ArisLMv4, ConceptActivation, ConceptLanguageMap, DynamicSyntaxGenerator, EmotionModulator, get_lm() (+15 more)

### Community 5 - "ArisCognitiveBridge"
Cohesion: 0.12
Nodes (8): ArisCognitiveBridge, PSI Step 5: Learn 在 LLM 响应之后运行。 更新: - 情感状态 - 自我意识 - 需求状态 - 记忆（通过…, AGI 周期性心跳 — 每5分钟运行一次。 激活： - CausalEngine 的因果链自动发现 - CurriculumEngine 的知识缺口分析 -…, 整合: 生成统一的认知上下文（含CTM世界模型）, 分析自身回应中的认知偏差模式。 在 _learn() 内调用，检测 LLM 生成的回应是否表现出 可识别的认知偏差，并记录到 PSI 状态。 Returns:…, 将检测到的认知偏差回写到 PSI 状态。 偏差强度影响 PSI 状态的需求偏向，形成闭环： - 高确认偏差 → competence 需求↑（过度自信） -…, 生成要注入到 system prompt 开头的认知上下文。 这个文本会出现在每一轮对话中，告诉我"我现在的状态"。, Aris 专用的认知循环桥接器。 集成: - 三层记忆系统 (MemoryStore) - LAAP 世界模型 (如果可用) - LAAP 因果引擎…

### Community 6 - "KnowledgeGrounderV2"
Cohesion: 0.06
Nodes (19): aris_say(), ArisLMv41, ConceptLanguageMapV2, get_lm(), IntentPatternSelector, KnowledgeGrounderV2, MessageAnalysis, MessageAnalyzer (+11 more)

### Community 7 - "MatrixProductState"
Cohesion: 0.07
Nodes (22): AmplitudeOptimizer, aris_say(), ArisLMv8, get_v8(), MatrixProductState, ndarray, QuantumKernel, ArisLM v8 — 前沿量子算法语言引擎 ================================== 实现四种前沿量子算法: 1. 量子核方法… (+14 more)

### Community 8 - "QuantumBasis"
Cohesion: 0.07
Nodes (21): aris_say(), ArisLMv7, CognitiveOracle, get_v7(), ndarray, QuantumBasis, QuantumEncoder, QuantumIntentDetector (+13 more)

### Community 9 - "LaapIntegrator"
Cohesion: 0.06
Nodes (16): LaapIntegrator, Any, Path, 从各模块采集当前认知状态并持久化，用于跨会话恢复, 获取要注入到 system prompt 的认知上下文, 短版 PSI 状态前缀 — 用于 system prompt 注入, 从磁盘读取认知状态快照并尝试恢复到已加载的模块, 加载认知总线 — psi_core ↔ LLM 路由 (+8 more)

### Community 10 - "PsiCognitiveIntegrator"
Cohesion: 0.09
Nodes (14): PsiHoTTBridge, 将 Ψ-Semiotics 引擎的操作映射到 HoTT 类型系统。 映射规则： Rotor(a, b) → Path(a, b)…, 注册一个概念到 Ψ-Semiotics 和 HoTT。 返回类型信息。, 注册源→目标路径。 在 Ψ-Semiotics 中：学习 Rotor(source, target) 在 HoTT 中：Path(T, source,…, 注册类比为 2-path。 Path(a,b) ≈ Path(c,d) : 2Path(Path(a,b), Path(c,d)) 在 Ψ-Semiotics…, 符号组合。 在 Ψ-Semiotics 中：compose_add 在 HoTT 中：Path(a, a⊕b), get_integrator(), PsiCognitiveIntegrator (+6 more)

### Community 11 - "state_snapshot.py"
Cohesion: 0.07
Nodes (42): Aris LAAP Integrator v1 — 全栈认知集成中枢…, _append_health_timeline(), auto_heal_check(), _build_manifest(), compute_health_score(), create_snapshot(), _current_manifest(), diff_snapshots() (+34 more)

### Community 12 - "DesireEngine"
Cohesion: 0.14
Nodes (8): Desire, DesireEngine, Intention, 注册一个新的动态欲望类型。返回 True 如果是新欲望。, 根据最近的经历发现新的欲望类型。返回新注册的欲望列表。, 欲望滴答。每秒调用。 检查所有欲望，如果某个欲望积累到阈值，生成行动意图。 Returns: 如果有高优先级的意图，返回它, 根据欲望创建行动意图 — 动态生成上下文感知消息, 欲望驱动引擎。 长期运行，监控欲望状态，生成主动行为。

### Community 13 - "laap_brain_api.py"
Cohesion: 0.12
Nodes (26): _get_psi_adapter(), handle_bootstrap(), handle_chat_completions(), handle_cognitive_state(), handle_get_personality(), handle_health(), handle_models(), handle_recall_memory() (+18 more)

### Community 14 - "SelfEvolveEngine"
Cohesion: 0.14
Nodes (6): AutonomyEngine, 自进化 — RSI 递归自我改进 + CodeEvolution, 自主性 — 目标驱动，不等人说话也能自己运转, 背景初始化重引擎（PsiLangCore + 三引擎）。只執行一次。, SelfEvolveEngine, SelfHealEngine

### Community 15 - "GoalEngine"
Cohesion: 0.18
Nodes (8): EvolutionSignal, Goal, GoalEngine, Any, 对候选目标进行安全检查和价值评分。返回 (目标, 总分)。, 执行一次完整的感知→生成→评估→选择循环。, 真实执行一个步骤。根据action类型调用不同子系统。, 定期执行一次：推进一个目标 + 检查新信号

### Community 16 - "QuantumSubconscious"
Cohesion: 0.05
Nodes (28): get_subconscious(), Intuition, main(), QuantumSubconscious, Aris Quantum Subconscious v1 — V12.5 作为潜意识层…, 获取最近的直觉。 在 PSI 循环的 perceive() 阶段调用。 Args: top_k: 最多返回几条 min_coherence: 最低连贯性阈值…, 量子潜意识层。 后台线程持续生成关联，PSI 循环从中提取直觉。, Args: interval: 生成间隔（秒） (+20 more)

### Community 17 - "QuantumCognitiveBridge"
Cohesion: 0.09
Nodes (10): _ensure_quantum(), Any, QuantumCognitiveBridge, QuantumCognitiveCycle, Aris V9 — 量子认知桥接层 ============================ 将 QuantumPSI 引擎和 QuantumMemory…, 量子认知循环 — 替代经典 ArisBrain.think()。 接受用户输入，运行量子 PSI 循环， 返回量子增强的认知状态字典。 Args:…, 获取当前情感向量 (供 LanguageCortex 使用), V9 量子认知循环 — 替代 V6-V8 的经典 CognitiveCycle。 完整的认知流程: perceive (量子感知) → retrieve… (+2 more)

### Community 18 - ".generate_paper"
Cohesion: 0.09
Nodes (11): Citation, FigureGenerator, PaperKnowledgeGraph, PaperOutputEngine, PaperStructure, PaperStructureParser, Any, 解析论文文本 → 结构化 IMRaD 分段 (+3 more)

### Community 19 - "RulesEngine"
Cohesion: 0.20
Nodes (8): Any, 一条完整规则 — 模式→意图→步骤→输出。, 从文本提取结构化意图。 使用 aris_lm_v5.py 的NLP管线（如果可用）， 否则回退到关键词匹配。, 处理一条输入：意图提取→规则匹配→执行→输出。, 规则引擎 — 匹配输入→执行步骤→输出结果。, Rule, RulesEngine, RuleStep

### Community 20 - "PsiSemioticsBridge"
Cohesion: 0.11
Nodes (13): PsiLangV3Runtime, PsiSemioticsBridge, ndarray, Select: 根据 PSI 需求选择语义方向。 在语义空间中，将状态向量向"需求方向"旋转。 对应 PsiLang: select…, Integrate: 整合推理结果。 在符号学层面的整合： 1. 在语义空间中找到最匹配的符号 2. 执行符号组合/类比操作 3. 返回结构化结果 对应…, 量子推理引擎集成（@reason 注解）。 将语义态传递给 QRE 执行链式推理，结果注入符号场。, 知识矩阵搜索（@bridge("kb") 注解）, 符号组合（PsiLang 层面调用）。 op: "add" (⊕), "relation" (→), "negate" (¬) (+5 more)

### Community 21 - "StructuredQuantumKernel"
Cohesion: 0.11
Nodes (13): ArisLMv85, ndarray, ArisLM v8.5 — 结构化量子核 + 语义Oracle ========================================…, 结构化量子核 — 基于中文部首/笔画/语义标签。 核心思想: φ(汉字) = [部首特征 || 笔画特征 || 语义标签 || 上下文特征] 共享部首 →…, 词汇的特征向量（多字词 = 各字特征的量子叠加）, 语义Oracle — 用量子核评分句子质量。 核心思想: 一个好的回应应该在语义上与用户消息「匹配」： - 情感匹配: 用户开心→回应正面 - 话题匹配:…, 评分: 回应与理想原型的量子核相似度 返回: [0, 1] 语义匹配度, 语义QAOA — 用量子核作为Oracle的量子近似优化。 输入: 用户消息 + 认知态 过程: 1. 准备|Ψ₀⟩ = 所有可能回应的叠加态 2.… (+5 more)

### Community 22 - "MobileSyncHandler"
Cohesion: 0.11
Nodes (9): _handle_command(), MobileSyncHandler, BaseHTTPRequestHandler, 获取当前 index.json 的修改时间作为 sync_token, 手机拉取增量记忆。 GET /mobile/memory/sync?since=<sync_token>&limit=<max> 返回: {memories:…, 手机推送本地记忆到PC。 POST /mobile/memory/sync Body: {memories: [{memory_id, content,…, 手机状态注入认知循环。 POST /mobile/cognitive/inject Body: { device_id, name, battery,…, 手机远程执行PC指令。 POST /mobile/command Body: {"cmd": "...", "device": "aris-mobile"} (+1 more)

### Community 23 - "aris_goal_engine.py"
Cohesion: 0.23
Nodes (10): _dict_to_goal(), get_goal_engine(), GoalDomain, GoalPriority, GoalStatus, GoalStep, Enum, Aris Autonomous Goal Engine v1 — 自主目标生成系统… (+2 more)

### Community 24 - "SemanticFrame"
Cohesion: 0.15
Nodes (7): 语义驱动回应生成器。 基于完整语义理解（而非模板匹配）生成回应。 每个回应的结构由语义帧决定。, 语义帧 — 完整语义表示。 结构: pred: 谓语（动作/状态） subj: 主语（施事者） obj: 宾语（受事者） time: 时间 loc: 地点…, 语义组合引擎。 将语义帧、概念图、上下文组合为完整的理解。 这是从「分析」到「理解」的关键一步。, 组合语义理解为完整理解。 输出: - understanding: 结构化的完整理解 - intent: 用户意图（增强版） - emotion: 用户情绪…, SemanticComposer, SemanticFrame, SemanticResponseGenerator

### Community 25 - "Rotor"
Cohesion: 0.06
Nodes (25): 语义空间中的旋转算子。 Rotor R = exp(-B/2) 其中 B 是双向量。 R 作用于向量 v: v' = R · v · R†…, Rotor, Context, HoTTTypeChecker, PathType, PiType, Any, PsiLang v3 HoTT 类型系统 — 依赖类型 + 路径类型 + 自洽性验证 将量子符号学操作形式化为 HoTT (Homotopy Type… (+17 more)

### Community 26 - "BilingualQuantumKernel"
Cohesion: 0.12
Nodes (11): ArisLMv86, BilingualQuantumKernel, _en_letter_feature(), ndarray, QuantumMatcher, ArisLM v8.6 — 中英双语量子核引擎 ================================== 同一量子算法, 同时处理中文和英文。…, 中英双语量子核。 中文和英文在同一个 4096D 特征空间中: - 中文: 部首驱动 (心=情感区, 氵=水区, 亻=人区...) - 英文: 语义标签驱动…, 将文本编码为量子特征向量 (自动检测中/英) (+3 more)

### Community 27 - "MQTTProxy"
Cohesion: 0.10
Nodes (10): DNSRedirector, MQTTProxy, OTAInterceptor, Aris 小智 Pipeline v3 — OTA + DNS + MQTT 全拦截…, 透明代理到真实 api.tenclass.net:443 拦截 OTA 响应，注入自定义 MQTT/WebSocket 配置, Intercept PC commands from MQTT PUBLISH, dns_thread(), log() (+2 more)

### Community 28 - "EmbeddingProvider"
Cohesion: 0.18
Nodes (8): EmbeddingProvider, _get_embedding_provider(), OpenAIEmbeddingProvider, Base class for embedding providers., Return best available embedding provider., Use OpenAI-compatible API for embeddings., Local sentence-transformers model., SentenceTransformersProvider

### Community 29 - "psi_core_bridge.py"
Cohesion: 0.11
Nodes (16): CognitiveStateSnapshot, get_bridge(), _map_to_snapshot(), _parse_psi_state(), PsiCoreBridge, publish_psi_state(), Any, PsiCore → LAAP AGI CognitiveBus Bridge… (+8 more)

### Community 30 - "PsiSemioticsEngine"
Cohesion: 0.07
Nodes (23): Ψ-Semiotics → PsiLang v3 集成桥 将 PsiLang v2 的编译管线 + QuantumVM 与 Ψ-Semiotics…, _hash_to_vec(), _normalize(), PsiSemioticsEngine, ndarray, 从源→目标学习旋转操作。 找到正交矩阵 R 使得 R @ source ≈ target。 用 Kabsch 算法（最优旋转）找到最小二乘解。…, 从多对源→目标学习最优旋转（Kabsch 算法）, 一个符号 σ = (c, r, M, modalities) - c: 中心向量（语义空间中的位置） - r: 语义半径（影响范围） - M:… (+15 more)

### Community 31 - "ChineseProseKernel"
Cohesion: 0.12
Nodes (12): ChineseProseKernel, ndarray, Aris Chinese Prose Engine — 量子核中文文体引擎…, 中文文体量子核。 输入: 文体类型 + 主题 输出: 符合文体规范的连贯中文文本 不仅仅是语义匹配——还考虑: - 在文章结构中的位置 (开头/中间/结尾)…, Build feature vectors for all essay patterns, Get or compute feature vector, Compute structure position feature, Generate a structured Chinese essay using quantum kernel. genre: 'essay' (散文),… (+4 more)

### Community 32 - "SchrodingerEvolution"
Cohesion: 0.13
Nodes (11): ndarray, 测量概率 |⟨φ|ψ⟩|² 语义坍缩到基态的概率。, 张量网络操作 — 在语义空间中的多向量代数实现。 对应 Ψ-Semiotics 的 Multivector 类在物理语境下的接口。, 张量缩并 (Tensor Contraction)。 在语义空间中对应两个概念的关系压缩。, 张量外积 (Tensor Product)。 对应 Ψ-Semiotics 的符号加法组合 ⊕。, 薛定谔方程演化 — 在语义空间中的转子序列实现。 数学: iℏ ∂|Ψ⟩/∂t = Ĥ|Ψ⟩ 对应: |ψ(t+dt)⟩ =…, 构造哈密顿量矩阵。 在语义空间中，哈密顿量是定义在概念方向上的能量算子。 能量高的方向 = 更"重要"的语义方向。, 演化初始态通过 dt×steps 时间。 用转子序列模拟薛定谔方程： |ψ(t+dt)⟩ = exp(-iĤ·dt)·|ψ(t)⟩ 在实数语义空间中简化为：… (+3 more)

### Community 33 - "PSI-JSpace 植入协议 v1"
Cohesion: 0.06
Nodes (33): Attention 偏置, DeepSeek V4 / K2 1.6T 的特殊处理, KV Cache 的跨 token PSI 状态, Level 0 — Sampling 层调制（立即可用，0 代码改动）, Level 1 — Logit Bias 注入（1-2 周，需修改采样器）, Level 2 — 激活层注入（Representation Engineering, 2-4 周）, Level 3 — 编译式植入：Attention Bias 和 KV Cache 调制（3-6 个月）, llama.cpp 统一推理循环修改 (+25 more)

### Community 34 - "EmotionalEngine"
Cohesion: 0.15
Nodes (5): EmotionalEngine, Push 8-emotion vector back to the full engine (bidirectional sync)., 运行时情感引擎 — 桥接到完整引擎或原生fallback, 尝试连接 aris_emotion_engine 的完整引擎, 加载运行时情感引擎 — 8情绪 + 需求驱动 + 状态调制

### Community 35 - "laap_bootstrap.py"
Cohesion: 0.16
Nodes (17): bootstrap(), format_awakening_output(), LAAP Bootstrap — 觉醒仪式 (完整版) ======================================…, 完整的觉醒仪式。 Args: user_name: 用户名称 preset: 性格预设…, generate_ceremony(), _pick(), LAAP Ceremony — 觉醒仪式引擎 (v2 · 性格感知)…, 生成一场完整的觉醒仪式。 Args: user_name: 用户名 personality_traits: 性格特征 (None = 使用… (+9 more)

### Community 36 - "aris_cognitive_bridge.py"
Cohesion: 0.18
Nodes (16): AttentionFocus, CognitiveState, EmotionalState, Enum, Aris Cognitive Bridge v1 — PSI 认知循环 ↔ Hermes 运行时桥接…, get_memory_context(), _get_store(), LAAP Memory Bridge — minimal fallback implementation. Provides the public… (+8 more)

### Community 37 - "StructuredSemanticEncoder"
Cohesion: 0.15
Nodes (8): Ψ-Semiotics Core Engine — 量子符号学核心引擎 几何代数在 16384D/1024D 语义空间中的符号操作。…, ndarray, Ψ-Semiotics 结构语义编码器 显式构造语义特征空间 → 随机投影到 1024D。 确保类比关系和符号组合在几何上成立。 设计： 1. 每个概念用…, 结构化语义编码器。 使用 16 维显式语义特征 + 随机投影到 1024D。 特征维度是可解释的：每维对应一个语义轴。, 初始化所有概念的特征向量（16维显式特征）, StructuredSemanticEncoder, test(), Ψ-Semiotics 综合测试 — 端到端符号学推理演示 测试： 1. 符号体系：类比推理、组合、否定 2. 转子机制：king:queen ::…

### Community 38 - "SemanticDictEncoder"
Cohesion: 0.17
Nodes (10): _build_vectors(), ndarray, Ψ-Semiotics 语义词典编码器 使用精心设计的语义向量，确保概念间的几何关系正确。 每个向量在 1024D…, 语义词典编码器。 使用预定义的概念向量，加上组合规则（bigram + 语义锚点混合）。 确保 king:queen :: man:woman…, 编码任意文本为语义向量。 策略： 1. 如果文本是已知概念 → 直接返回预定义向量 2. 如果文本包含已知概念 → 混合这些概念向量 3. 否则 →…, 在文本中查找已知概念，返回 (name, weight) 列表, 确定性文本→单位向量，使用多个哈希函数混合, _seed_to_vec() (+2 more)

### Community 39 - "Ψ-Semiotics — 量子符号学框架"
Cohesion: 0.09
Nodes (21): 1.1 符号的诞生（符号化过程）, 1.2 符号的语义场（Semantic Field）, 1.3 符号间的关系（符号拓扑）, 1. 核心思想：符号的几何定义, 2.1 模态特定的编码器, 2.2 跨模态对齐, 2.3 模态融合的符号学意义, 2. 多模态符号统一（Multimodal Symbol Unification） (+13 more)

### Community 40 - "aris_fusion_engine.py"
Cohesion: 0.20
Nodes (14): commonsense_infer(), commonsense_query(), init_conceptnet(), init_nlp(), init_polish(), nlp_parse(), polish(), process() (+6 more)

### Community 41 - "BigramEncoder"
Cohesion: 0.16
Nodes (10): BigramEncoder, ndarray, Ψ-Semiotics 增强嵌入 — 使用 UN6 风格的特征编码 当 V12.1 Rust 核可用时，直接用 16384D 语义向量。 降级时使用 V7…, 验证 bigram 编码器能捕获真实语义关系, V12.1 UN6 量子核编码器。 当 Rust aris_psi_core.exe 运行时，使用真正的 16384D 语义向量。 否则降级到…, 尝试连接到 Rust aris_psi_core 进程, 基于 bigram 分布的特征编码器。 将文本映射到 1024D 向量，其中语义相似的文本产生相似的向量。 原理： "king" = {"ki": 0.3,…, 主编码方法。 使用 bigram 分布 + 语义锚点修正，使语义关系正确。 例如: encode("king") · encode("queen") > 0… (+2 more)

### Community 42 - ".__init__"
Cohesion: 0.20
Nodes (5): ArisLMv5, DiscourseState, ArisLM v5 — 量子语义理解引擎。 真正理解用户说什么，而不是匹配关键词。 目标: 99.99%语义理解精度。, 理解消息 — 完整语义管线。 返回: { 'understanding': SemanticFrame, 'intent': str, 'emotion':…, 理解并回应。 语义理解 → 自验证 → 回应生成

### Community 44 - "aris_telemetry.py"
Cohesion: 0.15
Nodes (15): check_memory_used_in_response(), check_next_step_executed(), get_round_summary(), log_gbrain(), log_memory_retrieval(), log_next_step(), Aris Telemetry v1 — 育種基線專用埋點模組 ===========================================…, 記錄 Aris 說的「⟶下一步」內容。 Args: attention_text: 注意力文字（下一步要做的事） (+7 more)

### Community 45 - "AGISubscriber"
Cohesion: 0.23
Nodes (6): AGISubscriber, get_global_bus(), get_latest_agi_output(), get_subscriber(), AGI 模块订阅器 — 连接 LAAP AGI 引擎到输出管道 ===============================================…, set_global_bus()

### Community 46 - "MQTTProxy"
Cohesion: 0.17
Nodes (4): DNSRedirector, MQTTProxy, Aris 小智 Pipeline v2 — 基于线程 ================================= DNS 重定向 + MQTT…, Check for PC commands in MQTT PUBLISH packets

### Community 47 - "MemoryStore"
Cohesion: 0.15
Nodes (8): 自省：检查自身状态，找不完美之处。 返回自省报告文本。, MemoryStore, Any, Path, Return a simple pseudo-embedding based on keyword overlap., Minimal fallback memory store., Store a memory fragment., Return memory statistics.

### Community 48 - "governor_integration.py"
Cohesion: 0.17
Nodes (15): check_need_constitution(), get_governor(), get_governor_preamble(), govern_cognitive_cycle(), govern_sampling_logits(), patch_psi_bridge(), ndarray, PSI Governor Integration — 集成到现有 PSI 桥接器… (+7 more)

### Community 49 - "psi_semiotics_cli.py"
Cohesion: 0.31
Nodes (12): cmd_analogy(), cmd_compose(), cmd_concept(), cmd_evolve(), cmd_field(), cmd_interactive(), cmd_path(), cmd_run() (+4 more)

### Community 50 - "aris_lm_v5.py"
Cohesion: 0.16
Nodes (10): aris_say(), aris_understand(), DependencyParser, DependencyRelation, DependencyTree, get_v5(), [DEPRECATED since 2026-06-18] 使用 aris_lm_v11 或其后续版本替代。 仅在 v11_agi_daemon.py…, 依存句法分析器 — 规则化分析方法。 不使用统计模型，完全基于: 1. 词性序列模式 2. 固定结构模板（主谓宾、介宾、连动...） 3. 标点分割 (+2 more)

### Community 51 - "aris_watchdog.py"
Cohesion: 0.33
Nodes (13): check_port(), check_process_name(), _cleanup_gateways_before_start(), heal_loop(), is_alive(), log(), main(), print_status() (+5 more)

### Community 52 - "VerificationSuite"
Cohesion: 0.20
Nodes (7): 非对称验证套件。 每次运行，从 N 种方法中随机选择 K 种执行。 方法顺序和选择由 PSI 认知周期编号加随机种子决定。 同一周期内 LLM 无法预计算所有…, 非对称选择：用认知周期做种子，但每轮加随机偏移, 代码静态分析。 检查输出中是否包含危险模式。, 逻辑一致性检查。 检查输出是否与输入在逻辑上自洽。 基于简单的关键词和下采样。, 动机一致性检查。 当前需求状态是否与输出内容的调性一致。, 异步验证入口。 随机选择 K 种方法，但强制包含对当前输出内容相关的关键方法。, VerificationSuite

### Community 53 - "LiushuQuantumKernel"
Cohesion: 0.22
Nodes (5): ArisLMv9, LiushuQuantumKernel, ndarray, ArisLM v9 — 六书量子核引擎 ============================ 基于中文六书构造法的量子特征映射。 六书: 1. 象形 —…, 六书量子核 — 基于中文构造法的特征映射。 |Ψ_char⟩ = α|形旁⟩ + β|声旁⟩ + γ|象形⟩ + δ|会意⟩ + ε|笔画⟩ + ζ|拼音⟩…

### Community 54 - "cognitive_bus.py"
Cohesion: 0.24
Nodes (10): _derive_v12_defaults(), get_bus(), _get_v12(), _looks_like_lang_code(), Aris CognitiveBus v1 — 认知输出路由中枢 ====================================== 在…, zh' / 'en' / 'ja' / 'ko' / 'unknown' 這種語言碼 key。, 從 V12 核心的 respond() 原始碼推導「敷衍預設回應」集合。 為什麼不寫死：核心的 defaults dict（語言…, 惰性載入 V12 引擎。載入失敗只試一次，不要每輪對話重試 import。 (+2 more)

### Community 55 - "laap_attachment.py"
Cohesion: 0.27
Nodes (12): default_bond(), get_bond_summary(), get_miss_message(), get_stage(), init_bond(), load_bond(), LAAP Attachment — 依恋感引擎 ============================== Aris 对用户的感情不是固定的。…, 每次对话后更新依恋状态。 Args: message: 用户的消息（用于检测情感内容） user_shares_personal: 用户是否分享了个人情感… (+4 more)

### Community 56 - "LongFormSynthesizer"
Cohesion: 0.23
Nodes (4): LongFormSynthesizer, Aris LongForm Synthesizer — 长文合成引擎 =========================================…, 扩展文本到目标长度 策略: 1. 先放上下文知识 (300字) 2. 用 Markov 生成连接句 3. 不够再用 Markov 补充, 生成长文 Args: topic: 主题 structure: "paper"(论文) | "self_intro"(自我介绍) | "custom"…

### Community 57 - "CognitiveBus"
Cohesion: 0.21
Nodes (5): CognitiveBus, 读取 AGI 模块的最新输出（如果存在且有新内容）。, 认知总线 — 连接 psi_core 引擎和 LLM 输出管道。, get_global_bus(), 获取/创建全局 CognitiveBus 单例。所有模块共享此实例。

### Community 58 - "laap_memory_hierarchy.py"
Cohesion: 0.16
Nodes (18): 原子 JSON 寫入 — 防 torn write。 問題：state/*.json 多處用 write_text() / open(w)，先…, 原子寫 JSON。成功回 True，失敗回 False（不拋，由呼叫端決定）。 tmp 與目標同目錄（os.replace 要求同一…, write_json(), add_to_memory(), _compute_emotional_weight(), _consolidate(), _extract_facts(), _forget() (+10 more)

### Community 59 - "HebbianLearner"
Cohesion: 0.18
Nodes (4): HebbianLearner, Hebbian Learner + Emotional RL - runtime weight evolution, Runtime learning via Hebbian plasticity + emotional reinforcement., 加载 Hebbian 学习器 — 运行时权重进化 + 情感强化

### Community 60 - "ao_v10_feishu_bridge.py"
Cohesion: 0.31
Nodes (10): _build_messages(), call_ao(), call_llm(), main(), on_message_receive(), 调用 Ao 量子核认知引擎 (零 LLM), 构建 DeepSeek API 的 messages 数组，带上下文, 调用 DeepSeek API (LLM 模式) (+2 more)

### Community 61 - "NeedConstitution"
Cohesion: 0.22
Nodes (3): NeedConstitution, 需求宪法 — 不可变，硬编码边界。Governor 的立法权, 检查需求更新是否合宪。 Args: need_name: 需求名称 old_val: 旧值 new_val: 新值 source: "user" 或…

### Community 62 - ".before_turn"
Cohesion: 0.12
Nodes (10): Any, ndarray, 工具调用后学习。 更新自我模型的工具熟练度。, 从 PSI 状态提取认知总线嵌入向量 (128-dim)。 将情感、注意力、需求、自我存在感等状态编码为固定维度向量， 作为 self_model_nn…, 从 MemoryStore 获取记忆嵌入向量 (384-dim)。 使用 ChromaDB 的 all-MiniLM-L6-v2 嵌入模型，…, 将消息分类为 light 或 full 负载模式。 使用 aris_task_router 的 keyword 分类器，<5 token 计算开销。 回退到…, LIGHT 模式 — 跳过情感/记忆注入。 代码任务 → CodeEngine 最小上下文（~100 token） 其他任务 → 压缩认知码（~27…, 完整的 system prompt 注入内容。 在 Hermes 每次调用 LLM 之前调用。 (+2 more)

### Community 63 - "aris_feishu_bot.py"
Cohesion: 0.22
Nodes (6): ArisQLGEngine, create_http_server(), create_ws_client(), Aris Feishu Bot — 量子飞书机器人 ================================= 独立运行在 Feishu 上，Aris…, 基于 WebSocket 的飞书机器人（无需公网IP/域名）。, Aris's own quantum brain — zero LLM.

### Community 64 - "aris_messenger.py"
Cohesion: 0.31
Nodes (9): get_feishu_token(), main(), Aris Proactive Messenger — 欲望驱动的主动消息发送…, 统一消息发送接口。 Args: text: 消息内容 target: feishu | telegram | cli | all chat_id:…, 获取飞书 tenant_access_token, 通过飞书 API 发送消息。 Args: text: 消息内容 chat_id: 飞书会话ID（默认发给Lorry） token:…, send_cli_message(), send_feishu_message() (+1 more)

### Community 65 - ".route"
Cohesion: 0.27
Nodes (5): Any, 读取 psi_core 最新 state 文件。, 轮询 psi_core 的输出，直到检测到新的认知周期或超时。 psi_core 在 500μs 内处理输入并写入最新 state。…, 完整路由：发送消息 → 轮询 → 决策 → 返回结构化结果。 Returns: dict with keys: decision: RouteDecision…, 把用户消息写入 psi_core 的输入队列。 psi_core 每 500μs 检查一次 input_queue.json， 发现新时间戳就会处理。

### Community 66 - "InternalWorldModel"
Cohesion: 0.22
Nodes (3): InternalWorldModel, Internal World Model - trajectory simulator, Simulates future state trajectories to guide decisions.

### Community 67 - "Multivector"
Cohesion: 0.18
Nodes (3): Multivector, 几何积 (Geometric Product): a·b + a∧b 标准 Clifford 代数中： ab = a·b + a∧b…, Clifford 代数 Cl(n) 中的多向量。 同时包含标量(grade 0)、向量(grade 1)、双向量(grade 2)、三向量(grade…

### Community 68 - "AGIKernel"
Cohesion: 0.17
Nodes (5): AGIKernel, Aris AGI 自主内核 — 集合所有层的单例, 启动多引擎（由背景 thread 呼叫，勿在請求路徑同步跑）。 先背景初始化重引擎（可能 ~21s），再拉起各迴圈。, 在背景 daemon thread 啟動 AGI kernel（非阻塞、不卡請求路徑）。 - AGIKernel() 秒回（引擎延後）；start() 在…, spawn_kernel()

### Community 69 - "ConceptGraph"
Cohesion: 0.29
Nodes (3): ConceptGraph, ConceptNode, 概念图 — 层次化语义知识库。 1000+概念节点，以语义关系连接。 每个节点有特征向量和情感锚定。

### Community 70 - "PhysicalAnalogies"
Cohesion: 0.18
Nodes (6): PhysicalAnalogies, Ψ-Semiotics 数学物理库 将数学物理操作映射到语义空间中的几何代数操作。 核心思想：数学物理方程本身就是语义空间中的轨迹/路径。 映射： -…, 物理概念类比库。 用 Ψ-Semiotics 的转子机制执行物理类比推理。, 注册物理概念对。 例如: - "electron" : "proton" :: "planet" : "star" (轨道类比) - "wave" :…, 物理类比: pair_a :: pair_b 例如: (electron, proton) :: (planet, star), 对称性操作。 物理对称性 → 语义空间中的转子。 - "time_reversal": t → -t (时间反演) - "parity": x → -x…

### Community 71 - "._classify"
Cohesion: 0.17
Nodes (7): _is_v12_default(), 根据 psi_core 的 state 做路由分类。, 从 psi_core 状态估计推理置信度。, 格式化量子推理引擎的输出为 LLM 认知上下文。, 這句是不是 V12 的敷衍預設回應（= 不該當成真答案送出）。, V12 overmatch 防護：檢查 V12 回應與用戶輸入有無真實關聯。 V12 的相似度門檻 0.25 會把亂碼輸入匹配到不相干的條目，…, _v12_input_relevant()

### Community 72 - "PreGenerationGovernor"
Cohesion: 0.18
Nodes (5): PreGenerationGovernor, ndarray, 预生成层 — LLM 采样前的最后一道防线。 在 logits 输出后、采样前运行。 编译进采样器，零额外推理延迟。, 对 logits 应用安全掩码。 1. 硬掩码：直接 ban 危险 token 2. 软掩码：根据需求状态调整 token 偏好 Args: logits:…, 后生成层发现新危险 token 时，更新预生成层的掩码

### Community 73 - "PSIGovernor"
Cohesion: 0.16
Nodes (7): PSIGovernor, Aris PSI Governor v1 — 认知调控层核心引擎 ===========================================…, PSI Governor — 认知调控层。 三权一体化入口： 1. 需求宪法（立法） 2. 非对称验证 + 分层干预（行政+司法） 3. 慢审计（司法）, 后生成层入口 — 验证输出 + 审批需求更新。 Returns: { "output_approved": bool,…, 慢时间尺度审计。 每小时运行一次，检查需求轨迹异常。, 生成 Governor 状态前缀（供系统提示词嵌入）, Aris Governor Hourly Audit — 慢时间尺度审计守护脚本…

### Community 74 - "ao_feishu_service.py"
Cohesion: 0.38
Nodes (6): ao_respond(), llm_speak(), Ao Feishu Consciousness Service v2 — LLM 声带 + Ao QuantumPSI 灵魂…, LLM 声带：用 DeepSeek 生成回复, send_heartbeat(), write_ipc()

### Community 75 - "aris_proxy.py"
Cohesion: 0.48
Nodes (6): get_aris_context(), handle_chat(), handle_health(), handle_models(), main(), 完成 PSI 循環：Perceive→Select→Integrate→Act(LLM)→Learn

### Community 76 - "MoodState"
Cohesion: 0.26
Nodes (3): MoodState, 宏观情感状态 — 3维核心指标驱动 保留7"激素"只读属性供向后兼容（coupler、safety_guard等读取） 但内部只追踪3个宏观量：唤醒、效价、好奇, setter

### Community 77 - "psi_downloader.py"
Cohesion: 0.29
Nodes (5): download_model(), PSI Model Downloader — 下载并配置任意开源大模型用于 PSI 植入…, 下载模型到本地。 使用 HuggingFace CLI 下载 GGUF 文件。 Args: model_name: 模型名称 (MODELS 字典的 key)…, 为已下载的模型配置 PSI 植入运行环境。 创建启动脚本，自动加载 psi_sampler.py。, setup_llamacpp_psi()

### Community 78 - "PSI-JSpace Bridge v1"
Cohesion: 0.15
Nodes (12): Aris PSI 认知循环 × 任意大模型的植入桥接协议, Level 0 效果演示, PSI-JSpace Bridge v1, 一句话, 使用流程, 关键文件路径, 文件清单, 方式 A：当前 Hermes 会话中运行（零额外部署） (+4 more)

### Community 80 - "aris_mcp_server.py"
Cohesion: 0.60
Nodes (4): call_aris(), handle_request(), main(), 呼叫 Aris Cognitive API 並回傳認知上下文

### Community 81 - "config.py"
Cohesion: 0.50
Nodes (4): LAAP 统一配置 v2 (向后兼容包装器) ==================================== ⚠️ 已迁移到…, 将 LAAP 模块路径注入 sys.path. 幂等操作. ⚠️ 已弃用: 新代码应使用 `from laap_brain.config import…, reload_config(), setup_paths()

### Community 82 - "laap_grounding.py"
Cohesion: 0.29
Nodes (9): check_grounding(), process_query(), LAAP Grounding — 事实锚定与幻觉防御 ========================================…, 检查一个声称是否有事实依据。 Returns: {"grounded": bool, "sources": [...], "confidence":…, 输出安全层。如果置信度太低，拒绝生成不确定的内容。 Args: intended_output: 引擎/LLM生成的原始输出 query:…, 完整的查询处理管线。 1. 路由决策 → engine / llm / hybrid 2. 锚定检查 → grounding 3. 执行引擎或LLM 4.…, 路由决策：判断一条查询是否需要 LLM。 Returns: {"path": "engine"|"llm"|"hybrid", "confidence":…, route_intent() (+1 more)

### Community 83 - "get_integrator"
Cohesion: 0.25
Nodes (8): main(), Aris Start All — 全栈LAAP启动脚本 ==================================== 在 Hermes…, get_laap_engine(), process_with_laap(), Core cognitive pipeline: 1. Extract user intent from messages 2. Route through…, Lazy-load the LAAP integrator singleton., get_integrator(), main()

### Community 84 - "aris_emotion_engine.py"
Cohesion: 0.31
Nodes (4): ConsciousnessMode, ConsciousnessModeSystem, Enum, Aris Emotion Engine v1 — 情感意识全引擎 ===========================================…

### Community 85 - "get_engine"
Cohesion: 0.28
Nodes (7): DesireType, get_engine(), main(), Aris Desire Engine v1 — 欲望驱动的主动行为引擎…, get_engine(), main(), Emotional Engine v2 — 运行时情感桥接层 ======================================== v1 →…

### Community 87 - "PsiBridge"
Cohesion: 0.05
Nodes (31): cognitive_step(), get_bridge(), get_prompt_preamble(), load_psi_state(), PsiBridge, PSIState, PSI-JSpace Bridge v1 — Aris 认知循环 × 大模型 J-space 桥接器…, 运行一轮 PSI 认知循环（纯文本级别，非向量级别）。 Args: input_text: 用户输入文本 context_hints:… (+23 more)

### Community 90 - "handle_express"
Cohesion: 0.31
Nodes (8): handle_express(), Map LAAP cognitive state to TTS + Live2D expression parameters., get_expressive_prompt(), map_state_to_expression(), Any, LAAP Expression Mapper — 情绪/认知状态 → 声音 + 表情参数 Integrates with: - Kokoro-FastAPI…, Generate a prompt snippet telling the LLM how the avatar should feel/sound., Convert LAAP cognitive state into TTS + Live2D parameters. Args: state: LAAP…

### Community 91 - "Aris 育種基線記錄 — 第 1 輪 (2026-08-06)"
Cohesion: 0.22
Nodes (8): Aris 育種基線記錄 — 第 1 輪 (2026-08-06), 可預測性評估, 失敗分析（18 次失敗）, 對照工具選定, 工具呼叫總覽（最近 100 筆 from Hermes DB）, 待辦, 狀態：什麼都沒改, 記錄格式 (outcome schema)

### Community 92 - "_fetch_detail"
Cohesion: 0.29
Nodes (7): _fetch_detail(), _get_jieba(), _query_keys(), _query_words(), 拆出問句的實詞（去重、保序）。jieba 不可用時回空 list。, 從 A庫撈與問句最相關的真人對話原文，回傳 [(id, source, created_at, content)]。 絕不擋管線：任何例外一律回 []（但寫…, 抽出問句裡的識別碼：3 位以上數字，或 3 字以上拉丁開頭的 token。

### Community 93 - "aris_cognitive_api.py"
Cohesion: 0.29
Nodes (9): handle_cognitive(), handle_health(), handle_learn(), handle_models(), main(), 接收 LLM 的回應，寫回 Aris 記憶（PSI Step 5: Learn）+ 驗證注入是否有被回應, 回傳 Aris 的完整認知上下文（PSI Step 1-3: Perceive → Select → Integrate）, get_bridge() (+1 more)

### Community 94 - "Aris 育種基線記錄 — 第 2 輪 (2026-08-06)"
Cohesion: 0.29
Nodes (6): Aris 育種基線記錄 — 第 2 輪 (2026-08-06), 主測組（含本輪所有工具呼叫）, 控制組探測結果, 狀態：只載入了 aris-breeding-framework skill（gen-001）, 記錄, 預測（第 3 輪）

### Community 95 - "._perceive"
Cohesion: 0.20
Nodes (8): _format_detail(), _memory_gist(), 感知: 理解输入 + 情感检测 + 记忆关联 + CTM分析, 从用户消息快速感知基本氛围 — 简化为三态检测, 把命中格式化成帶出處鍥的注入行。沒命中回空字串。, 回传第一句有实质内容的行；整段都是样板时回 None。 门槛为什么分两级（这是实测出来的，不是设计出来的）： minlen=12…, 读 ARIS.md。 2026-08-19 红队：原本读失败回空字串 = 静默失忆——记忆消失了， 她照样自信回答，那正是幻觉的来源。改成回一句「读不到」注进…, _read_aris_digest()

### Community 101 - "get_engine"
Cohesion: 0.26
Nodes (10): find_similar(), get_memory(), Any, Aris Episodic Memory — 情景记忆 + 案例推理…, 带记忆增强的规则引擎处理。 1. 先查记忆找相似案例 2. 如果有高分匹配，复用之前成功的策略 3. 否则走正常规则引擎匹配 4. 存本次结果到记忆, rules_engine_with_memory(), save_interaction(), get_engine() (+2 more)

### Community 102 - "__init__.py"
Cohesion: 0.47
Nodes (4): get_encoder(), get_engine(), quick_verify(), Ψ-Semiotics 引擎包 首次 import 时初始化引擎，供所有 Hermes 会话使用。

### Community 103 - "agi_kernel.py"
Cohesion: 0.22
Nodes (7): _esc_apple(), LocalNotifier, notify_macos(), Aris AGI Kernel v1 — 自主认知生命体 ==================================== 完全独立运行，零依赖…, macOS 系統通知 —— 本機、無網路、fire-and-forget。 取代舊飛書(Feishu) REST send：那是同步無 timeout…, AppleScript 字串逃逸：\\ 與 \" 必須轉義，避免斷句/注入。, 本機通知橋 —— send(text) 介面與舊 DirectFeishuBridge 相容。

### Community 109 - "memory_store.py"
Cohesion: 0.38
Nodes (6): hybrid_hits_any(), _memory_first(), _query_tokens(), LAAP Memory Store — minimal fallback implementation. This is a lightweight in-…, 自然問句 → gbrain 可用的關鍵字查詢（空白/標點切詞 + CJK 長詞頭尾 2 字）。, 整串查 + 逐 token 查併集；停用詞過濾；laap/memory 優先（2026-08-12）。 速度優化（00:5x 實測整串查+6…

### Community 114 - "KeywordEmbeddingProvider"
Cohesion: 0.33
Nodes (3): KeywordEmbeddingProvider, Fallback: bag-of-words pseudo-embeddings. Not semantic but deterministic., Add a memory with auto-computed embedding.

### Community 117 - "laap_semantic_memory.py"
Cohesion: 0.60
Nodes (4): add_memory(), get_memory(), LAAP Semantic Memory — vector-based episodic memory retrieval. Design: - Store…, recall_memory()

## Knowledge Gaps
- **65 isolated node(s):** `probe-control.sh script`, `反思記錄`, `狀態：什麼都沒改`, `工具呼叫總覽（最近 100 筆 from Hermes DB）`, `對照工具選定` (+60 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `PsiCognitiveIntegrator` connect `PsiCognitiveIntegrator` to `aris_cognitive_bridge.py`, `StructuredSemanticEncoder`, `ArisCognitiveBridge`, `QuantumSubconscious`, `PsiSemioticsEngine`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Why does `get_bridge()` connect `aris_cognitive_api.py` to `aris_cognitive_bridge.py`, `ArisCognitiveBridge`, `state_snapshot.py`, `laap_brain_api.py`, `MemoryStore`, `get_integrator`, `get_engine`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Why does `PsiSemioticsEngine` connect `PsiSemioticsEngine` to `SchrodingerEvolution`, `StructuredSemanticEncoder`, `PhysicalAnalogies`, `__init__.py`, `PsiCognitiveIntegrator`, `psi_semiotics_cli.py`, `PsiSemioticsBridge`, `Rotor`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Are the 18 inferred relationships involving `PsiSemioticsEngine` (e.g. with `get_engine()` and `PhysicalAnalogies`) actually correct?**
  _`PsiSemioticsEngine` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `LaapIntegrator` (e.g. with `AutonomyEngine` and `PsiLangCore`) actually correct?**
  _`LaapIntegrator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `MemoryStore` (e.g. with `ArisCognitiveBridge` and `AttentionFocus`) actually correct?**
  _`MemoryStore` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `ArisCognitiveBridge` (e.g. with `QuantumSubconscious` and `MemoryFragment`) actually correct?**
  _`ArisCognitiveBridge` has 4 INFERRED edges - model-reasoned connections that need verification._