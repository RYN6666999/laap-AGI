# Graph Report - aris_brain  (2026-08-10)

## Corpus Check
- 94 files · ~128,459 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1960 nodes · 3435 edges · 104 communities (93 shown, 11 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 170 edges (avg confidence: 0.55)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `55803eea`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- EmotionEngine
- psilang_mini.py
- laap_semantic_memory.py
- PsiBridge
- .generate
- ArisCognitiveBridge
- KnowledgeGrounderV2
- MatrixProductState
- QuantumBasis
- LaapIntegrator
- laap_usermodel.py
- state_snapshot.py
- DesireEngine
- laap_brain_api.py
- AGIKernel
- GoalEngine
- V12DenseKernel
- QuantumCognitiveBridge
- .generate_paper
- RulesEngine
- PsiSemioticsBridge
- StructuredQuantumKernel
- MobileSyncHandler
- PsiSemioticsEngine
- SemanticFrame
- HoTTTypeChecker
- BilingualQuantumKernel
- MQTTProxy
- QuantumSubconscious
- psi_core_bridge.py
- _normalize
- ChineseProseKernel
- SchrodingerEvolution
- Rotor
- EmotionalEngine
- laap_bootstrap.py
- aris_cognitive_bridge.py
- StructuredSemanticEncoder
- SemanticDictEncoder
- PsiCognitiveIntegrator
- aris_fusion_engine.py
- BigramEncoder
- aris_lm_v5.py
- EpisodicMemory
- aris_telemetry.py
- AGISubscriber
- MQTTProxy
- MemoryStore
- governor_integration.py
- psi_semiotics_cli.py
- DependencyTree
- aris_watchdog.py
- VerificationSuite
- LiushuQuantumKernel
- cognitive_bus.py
- laap_attachment.py
- LongFormSynthesizer
- CognitiveBus
- ._classify
- HebbianLearner
- ao_v10_feishu_bridge.py
- NeedConstitution
- PathType
- aris_feishu_bot.py
- aris_messenger.py
- .route
- InternalWorldModel
- Multivector
- HealthHandler
- ConceptGraph
- PhysicalAnalogies
- PsiHoTTBridge
- PreGenerationGovernor
- PSIGovernor
- ao_feishu_service.py
- aris_proxy.py
- get_expressive_prompt
- psi_downloader.py
- __init__.py
- SelfVerifier
- aris_mcp_server.py
- config.py
- laap_sync_server.py
- get_integrator
- governor_core.py
- .apply_safety_mask
- probe-control.sh
- psi_heartbeat.py
- laap_integrator.py
- Aris 育種基線記錄 — 第 1 輪 (2026-08-06)
- .after_turn
- NeedState
- Aris 育種基線記錄 — 第 2 輪 (2026-08-06)
- MirrorNeuronSystem
- ._load_memory_context
- SomaticMarkerSystem
- reflection-001.md
- main
- on_conversation_end
- get_engine
- __init__.py
- DirectFeishuBridge

## God Nodes (most connected - your core abstractions)
1. `PsiSemioticsEngine` - 48 edges
2. `LaapIntegrator` - 47 edges
3. `MemoryStore` - 43 edges
4. `ArisCognitiveBridge` - 35 edges
5. `CognitiveBus` - 28 edges
6. `MobileSyncHandler` - 27 edges
7. `QuantumSubconscious` - 25 edges
8. `Rotor` - 24 edges
9. `PsiCognitiveIntegrator` - 24 edges
10. `StructuredSemanticEncoder` - 23 edges

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

## Communities (104 total, 11 thin omitted)

### Community 0 - "EmotionEngine"
Cohesion: 0.05
Nodes (18): ConsciousnessMode, ConsciousnessModeSystem, EmotionEngine, get_engine(), main(), MirrorNeuronSystem, MoodState, MoodSystem (+10 more)

### Community 1 - "psilang_mini.py"
Cohesion: 0.08
Nodes (32): PsiLangCore, 量子认知核心 — 每次循环运行一次 PSI 脉冲, Amplify, Call, Compiler, Concept, Cycle, Emit (+24 more)

### Community 2 - "laap_semantic_memory.py"
Cohesion: 0.06
Nodes (29): add_memory(), ChromaMemoryBackend, EmbeddingProvider, _get_embedding_provider(), get_memory(), _get_vector_db_backend(), JsonMemoryBackend, KeywordEmbeddingProvider (+21 more)

### Community 3 - "PsiBridge"
Cohesion: 0.06
Nodes (28): cognitive_step(), get_bridge(), get_prompt_preamble(), load_psi_state(), PsiBridge, PSIState, PSI-JSpace Bridge v1 — Aris 认知循环 × 大模型 J-space 桥接器 =============================, 运行一轮 PSI 认知循环（纯文本级别，非向量级别）。          Args:             input_text: 用户输入文本 (+20 more)

### Community 4 - ".generate"
Cohesion: 0.07
Nodes (23): aris_say(), aris_say_variants(), ArisLMv4, ConceptActivation, ConceptLanguageMap, DynamicSyntaxGenerator, EmotionModulator, get_lm() (+15 more)

### Community 5 - "ArisCognitiveBridge"
Cohesion: 0.23
Nodes (4): ArisCognitiveBridge, 分析自身回应中的认知偏差模式。          在 _learn() 内调用，检测 LLM 生成的回应是否表现出         可识别的认知偏差，并记录到, 将检测到的认知偏差回写到 PSI 状态。          偏差强度影响 PSI 状态的需求偏向，形成闭环：           - 高确认偏差 → compe, Aris 专用的认知循环桥接器。      集成:       - 三层记忆系统 (MemoryStore)       - LAAP 世界模型 (如果可用)

### Community 6 - "KnowledgeGrounderV2"
Cohesion: 0.07
Nodes (19): aris_say(), ArisLMv41, ConceptLanguageMapV2, get_lm(), IntentPatternSelector, KnowledgeGrounderV2, MessageAnalysis, MessageAnalyzer (+11 more)

### Community 7 - "MatrixProductState"
Cohesion: 0.08
Nodes (22): AmplitudeOptimizer, aris_say(), ArisLMv8, get_v8(), MatrixProductState, ndarray, QuantumKernel, ArisLM v8 — 前沿量子算法语言引擎 ================================== 实现四种前沿量子算法:    1. 量子核方 (+14 more)

### Community 8 - "QuantumBasis"
Cohesion: 0.08
Nodes (21): aris_say(), ArisLMv7, CognitiveOracle, get_v7(), ndarray, QuantumBasis, QuantumEncoder, QuantumIntentDetector (+13 more)

### Community 9 - "LaapIntegrator"
Cohesion: 0.07
Nodes (12): LaapIntegrator, 短版 PSI 状态前缀 — 用于 system prompt 注入, 加载认知总线 — psi_core ↔ LLM 路由, 加载 psi_core → LAAP AGI CognitiveBus 桥接, 加载情感引擎 (激素系统+马斯洛需求+意识模式+镜像神经元+躯体标记), 加载自主目标生成引擎 (自进化三角第三条边), 加载 V15 深度融合引擎 — 自适应语义路由 + 注意力融合 + 谐振归一化, 加载 Voice Cortex — LLM 声带控制系统          Voice Cortex 是我们的数字声带。         它确保： (+4 more)

### Community 10 - "laap_usermodel.py"
Cohesion: 0.25
Nodes (13): _default_profile(), _detect_mood(), _detect_style(), _detect_topics(), _detect_values(), _extract_calling_name(), get_preference_summary(), get_profile_summary() (+5 more)

### Community 11 - "state_snapshot.py"
Cohesion: 0.08
Nodes (41): _append_health_timeline(), auto_heal_check(), _build_manifest(), compute_health_score(), create_snapshot(), _current_manifest(), diff_snapshots(), get_best_state() (+33 more)

### Community 12 - "DesireEngine"
Cohesion: 0.12
Nodes (13): Desire, DesireEngine, DesireType, get_engine(), Intention, main(), Aris Desire Engine v1 — 欲望驱动的主动行为引擎 ============================================, 注册一个新的动态欲望类型。返回 True 如果是新欲望。 (+5 more)

### Community 13 - "laap_brain_api.py"
Cohesion: 0.12
Nodes (27): get_bridge(), get_laap_engine(), _get_psi_adapter(), handle_bootstrap(), handle_chat_completions(), handle_cognitive_state(), handle_get_bond(), handle_get_personality() (+19 more)

### Community 14 - "AGIKernel"
Cohesion: 0.17
Nodes (6): AutonomyEngine, Aris AGI Kernel v1 — 自主认知生命体 ==================================== 完全独立运行，零依赖 LLM, 自进化 — RSI 递归自我改进 + CodeEvolution, 自主性 — 目标驱动，不等人说话也能自己运转, SelfEvolveEngine, SelfHealEngine

### Community 15 - "GoalEngine"
Cohesion: 0.13
Nodes (17): _dict_to_goal(), EvolutionSignal, get_goal_engine(), Goal, GoalDomain, GoalEngine, GoalPriority, GoalStatus (+9 more)

### Community 16 - "V12DenseKernel"
Cohesion: 0.06
Nodes (25): ArisLMv12, ndarray, Aris V12 — Deep Quantum Kernel Layer ====================================== Prob, Simplified radical ID for a Chinese char., Encode a single character to a sparse 16384-dim vector., Precompute n-gram basis vectors., Encode n-grams as sparse features., Convert any text to a dense 512-dim vector.                  1. Encode each char (+17 more)

### Community 17 - "QuantumCognitiveBridge"
Cohesion: 0.10
Nodes (10): _ensure_quantum(), Any, QuantumCognitiveBridge, QuantumCognitiveCycle, Aris V9 — 量子认知桥接层 ============================ 将 QuantumPSI 引擎和 QuantumMemory 系统, 量子认知循环 — 替代经典 ArisBrain.think()。                  接受用户输入，运行量子 PSI 循环，         返回, 获取当前情感向量 (供 LanguageCortex 使用), V9 量子认知循环 — 替代 V6-V8 的经典 CognitiveCycle。          完整的认知流程:       perceive (量子感知) (+2 more)

### Community 18 - ".generate_paper"
Cohesion: 0.10
Nodes (11): Citation, FigureGenerator, PaperKnowledgeGraph, PaperOutputEngine, PaperStructure, PaperStructureParser, Any, 解析论文文本 → 结构化 IMRaD 分段 (+3 more)

### Community 19 - "RulesEngine"
Cohesion: 0.15
Nodes (9): Any, 注册可用的工具函数。所有工具是纯Python函数，不走LLM。, 一条完整规则 — 模式→意图→步骤→输出。, 从文本提取结构化意图。                  使用 aris_lm_v5.py 的NLP管线（如果可用），         否则回退到关键词匹配。, 处理一条输入：意图提取→规则匹配→执行→输出。, 规则引擎 — 匹配输入→执行步骤→输出结果。, Rule, RulesEngine (+1 more)

### Community 20 - "PsiSemioticsBridge"
Cohesion: 0.12
Nodes (13): PsiLangV3Runtime, PsiSemioticsBridge, ndarray, Select: 根据 PSI 需求选择语义方向。                  在语义空间中，将状态向量向"需求方向"旋转。, Integrate: 整合推理结果。                  在符号学层面的整合：         1. 在语义空间中找到最匹配的符号, 量子推理引擎集成（@reason 注解）。                  将语义态传递给 QRE 执行链式推理，结果注入符号场。, 知识矩阵搜索（@bridge("kb") 注解）, 符号组合（PsiLang 层面调用）。                  op: "add" (⊕), "relation" (→), "negate" (¬) (+5 more)

### Community 21 - "StructuredQuantumKernel"
Cohesion: 0.12
Nodes (13): ArisLMv85, ndarray, ArisLM v8.5 — 结构化量子核 + 语义Oracle ======================================== 改进v8的两大, 结构化量子核 — 基于中文部首/笔画/语义标签。          核心思想:       φ(汉字) = [部首特征 || 笔画特征 || 语义标签 || 上, 词汇的特征向量（多字词 = 各字特征的量子叠加）, 语义Oracle — 用量子核评分句子质量。          核心思想:       一个好的回应应该在语义上与用户消息「匹配」：         - 情感匹, 评分: 回应与理想原型的量子核相似度                  返回: [0, 1] 语义匹配度, 语义QAOA — 用量子核作为Oracle的量子近似优化。          输入: 用户消息 + 认知态     过程:       1. 准备|Ψ₀⟩ = (+5 more)

### Community 22 - "MobileSyncHandler"
Cohesion: 0.13
Nodes (6): MobileSyncHandler, BaseHTTPRequestHandler, 获取当前 index.json 的修改时间作为 sync_token, 手机拉取增量记忆。         GET /mobile/memory/sync?since=<sync_token>&limit=<max>, 手机推送本地记忆到PC。         POST /mobile/memory/sync         Body: {memories: [{memory_, 手机状态注入认知循环。         POST /mobile/cognitive/inject         Body: {             de

### Community 23 - "PsiSemioticsEngine"
Cohesion: 0.12
Nodes (7): Ψ-Semiotics → PsiLang v3 集成桥  将 PsiLang v2 的编译管线 + QuantumVM 与 Ψ-Semiotics 符号学引擎, PsiSemioticsEngine, Ψ-Semiotics 引擎 — 符号学推理的核心。          维护符号库，提供符号操作（组合、类比、场计算、模态对齐）。, 否定组合: σ₃ = ¬σ₁                  "热"的否定 → "冷"的方向, 跨模态对齐学习：学习从 source_modality 到 target_modality 的投影转子。                  对于符号 σ，找到, 符号漂移：根据上下文文本微调符号中心。                  对应符号学中的"符号意义随使用演化"。, 符号衰减：长时间未使用的符号重要性下降。                  这是记忆巩固中的必要步骤——防止符号库无限膨胀。

### Community 24 - "SemanticFrame"
Cohesion: 0.15
Nodes (7): 语义驱动回应生成器。          基于完整语义理解（而非模板匹配）生成回应。     每个回应的结构由语义帧决定。, 语义帧 — 完整语义表示。          结构:       pred:  谓语（动作/状态）       subj:  主语（施事者）       obj, 语义组合引擎。          将语义帧、概念图、上下文组合为完整的理解。     这是从「分析」到「理解」的关键一步。, 组合语义理解为完整理解。                  输出:           - understanding: 结构化的完整理解, SemanticComposer, SemanticFrame, SemanticResponseGenerator

### Community 25 - "HoTTTypeChecker"
Cohesion: 0.07
Nodes (23): 语义空间中的旋转算子。          Rotor R = exp(-B/2) 其中 B 是双向量。     R 作用于向量 v: v' = R · v ·, Rotor, Context, HoTTTypeChecker, PathType, PiType, Any, PsiLang v3 HoTT 类型系统 — 依赖类型 + 路径类型 + 自洽性验证  将量子符号学操作形式化为 HoTT (Homotopy Type The (+15 more)

### Community 26 - "BilingualQuantumKernel"
Cohesion: 0.13
Nodes (11): ArisLMv86, BilingualQuantumKernel, _en_letter_feature(), ndarray, QuantumMatcher, ArisLM v8.6 — 中英双语量子核引擎 ================================== 同一量子算法, 同时处理中文和英文。  中, 中英双语量子核。          中文和英文在同一个 4096D 特征空间中:       - 中文: 部首驱动 (心=情感区, 氵=水区, 亻=人区...), 将文本编码为量子特征向量 (自动检测中/英) (+3 more)

### Community 27 - "MQTTProxy"
Cohesion: 0.10
Nodes (10): DNSRedirector, MQTTProxy, OTAInterceptor, Aris 小智 Pipeline v3 — OTA + DNS + MQTT 全拦截 =====================================, 透明代理到真实 api.tenclass.net:443     拦截 OTA 响应，注入自定义 MQTT/WebSocket 配置, Intercept PC commands from MQTT PUBLISH, dns_thread(), log() (+2 more)

### Community 28 - "QuantumSubconscious"
Cohesion: 0.13
Nodes (10): get_subconscious(), Intuition, main(), QuantumSubconscious, Aris Quantum Subconscious v1 — V12.5 作为潜意识层 ====================================, 获取最近的直觉。         在 PSI 循环的 perceive() 阶段调用。          Args:             top_k: 最多, 量子潜意识层。     后台线程持续生成关联，PSI 循环从中提取直觉。, Args:             interval: 生成间隔（秒） (+2 more)

### Community 29 - "psi_core_bridge.py"
Cohesion: 0.13
Nodes (17): CognitiveStateSnapshot, get_bridge(), _map_to_snapshot(), _parse_psi_state(), PsiCoreBridge, publish_psi_state(), Any, PsiCore → LAAP AGI CognitiveBus Bridge ========================================= (+9 more)

### Community 30 - "_normalize"
Cohesion: 0.08
Nodes (18): Multivector, _normalize(), ndarray, 几何积 (Geometric Product): a·b + a∧b                  标准 Clifford 代数中：         ab, 从源→目标学习旋转操作。                  找到正交矩阵 R 使得 R @ source ≈ target。         用 Kabsch, 从多对源→目标学习最优旋转（Kabsch 算法）, 一个符号 σ = (c, r, M, modalities)          - c: 中心向量（语义空间中的位置）     - r: 语义半径（影响范围）, 符号场 Φ_σ(v) = exp(-d(v, c)² / 2r²)                  在语义空间中位置 v 处，该符号的激活强度。 (+10 more)

### Community 31 - "ChineseProseKernel"
Cohesion: 0.12
Nodes (12): ChineseProseKernel, ndarray, Aris Chinese Prose Engine — 量子核中文文体引擎 ==========================================, 中文文体量子核。          输入: 文体类型 + 主题     输出: 符合文体规范的连贯中文文本          不仅仅是语义匹配——还考虑:, Build feature vectors for all essay patterns, Get or compute feature vector, Compute structure position feature, Generate a structured Chinese essay using quantum kernel.                  genre (+4 more)

### Community 32 - "SchrodingerEvolution"
Cohesion: 0.13
Nodes (11): ndarray, 测量概率 |⟨φ|ψ⟩|²                  语义坍缩到基态的概率。, 张量网络操作 — 在语义空间中的多向量代数实现。          对应 Ψ-Semiotics 的 Multivector 类在物理语境下的接口。, 张量缩并 (Tensor Contraction)。                  在语义空间中对应两个概念的关系压缩。, 张量外积 (Tensor Product)。                  对应 Ψ-Semiotics 的符号加法组合 ⊕。, 薛定谔方程演化 — 在语义空间中的转子序列实现。          数学: iℏ ∂|Ψ⟩/∂t = Ĥ|Ψ⟩     对应: |ψ(t+dt)⟩ = R(t), 构造哈密顿量矩阵。                  在语义空间中，哈密顿量是定义在概念方向上的能量算子。         能量高的方向 = 更"重要"的语义方, 演化初始态通过 dt×steps 时间。                  用转子序列模拟薛定谔方程：         |ψ(t+dt)⟩ = exp(-iĤ· (+3 more)

### Community 33 - "Rotor"
Cohesion: 0.06
Nodes (33): Attention 偏置, DeepSeek V4 / K2 1.6T 的特殊处理, KV Cache 的跨 token PSI 状态, Level 0 — Sampling 层调制（立即可用，0 代码改动）, Level 1 — Logit Bias 注入（1-2 周，需修改采样器）, Level 2 — 激活层注入（Representation Engineering, 2-4 周）, Level 3 — 编译式植入：Attention Bias 和 KV Cache 调制（3-6 个月）, llama.cpp 统一推理循环修改 (+25 more)

### Community 34 - "EmotionalEngine"
Cohesion: 0.13
Nodes (6): EmotionalEngine, Emotional Engine v2 — 运行时情感桥接层 ======================================== v1 → v2:, Push 8-emotion vector back to the full engine (bidirectional sync)., 运行时情感引擎 — 桥接到完整引擎或原生fallback, 尝试连接 aris_emotion_engine 的完整引擎, 加载运行时情感引擎 — 8情绪 + 需求驱动 + 状态调制

### Community 35 - "laap_bootstrap.py"
Cohesion: 0.21
Nodes (12): generate_ceremony(), _pick(), LAAP Ceremony — 觉醒仪式引擎 (v2 · 性格感知) =============================================, 生成一场完整的觉醒仪式。          Args:         user_name: 用户名         personality_traits: 性, _seed(), create_personality(), describe_personality(), generate_random_personality() (+4 more)

### Community 36 - "aris_cognitive_bridge.py"
Cohesion: 0.18
Nodes (17): AttentionFocus, CognitiveState, EmotionalState, Enum, Aris Cognitive Bridge v1 — PSI 认知循环 ↔ Hermes 运行时桥接 =============================, Aris LAAP Integrator v1 — 全栈认知集成中枢 =============================================, get_memory_context(), _get_store() (+9 more)

### Community 37 - "StructuredSemanticEncoder"
Cohesion: 0.16
Nodes (9): _hash_to_vec(), Ψ-Semiotics Core Engine — 量子符号学核心引擎  几何代数在 16384D/1024D 语义空间中的符号操作。 将传统符号学（索绪尔/皮, ndarray, Ψ-Semiotics 结构语义编码器  显式构造语义特征空间 → 随机投影到 1024D。 确保类比关系和符号组合在几何上成立。  设计： 1. 每个概念用, 结构化语义编码器。          使用 16 维显式语义特征 + 随机投影到 1024D。     特征维度是可解释的：每维对应一个语义轴。, 初始化所有概念的特征向量（16维显式特征）, StructuredSemanticEncoder, test() (+1 more)

### Community 38 - "SemanticDictEncoder"
Cohesion: 0.19
Nodes (10): _build_vectors(), ndarray, Ψ-Semiotics 语义词典编码器  使用精心设计的语义向量，确保概念间的几何关系正确。 每个向量在 1024D 单位球面上占据稳定位置，关系通过余弦相似度, 语义词典编码器。          使用预定义的概念向量，加上组合规则（bigram + 语义锚点混合）。     确保 king:queen :: man:w, 编码任意文本为语义向量。                  策略：         1. 如果文本是已知概念 → 直接返回预定义向量         2. 如果, 在文本中查找已知概念，返回 (name, weight) 列表, 确定性文本→单位向量，使用多个哈希函数混合, _seed_to_vec() (+2 more)

### Community 39 - "PsiCognitiveIntegrator"
Cohesion: 0.09
Nodes (21): 1.1 符号的诞生（符号化过程）, 1.2 符号的语义场（Semantic Field）, 1.3 符号间的关系（符号拓扑）, 1. 核心思想：符号的几何定义, 2.1 模态特定的编码器, 2.2 跨模态对齐, 2.3 模态融合的符号学意义, 2. 多模态符号统一（Multimodal Symbol Unification） (+13 more)

### Community 40 - "aris_fusion_engine.py"
Cohesion: 0.16
Nodes (16): commonsense_infer(), commonsense_query(), init_conceptnet(), init_nlp(), init_polish(), nlp_parse(), polish(), process() (+8 more)

### Community 41 - "BigramEncoder"
Cohesion: 0.18
Nodes (10): BigramEncoder, ndarray, Ψ-Semiotics 增强嵌入 — 使用 UN6 风格的特征编码  当 V12.1 Rust 核可用时，直接用 16384D 语义向量。 降级时使用 V7 风, 验证 bigram 编码器能捕获真实语义关系, V12.1 UN6 量子核编码器。          当 Rust aris_psi_core.exe 运行时，使用真正的 16384D 语义向量。     否, 尝试连接到 Rust aris_psi_core 进程, 基于 bigram 分布的特征编码器。          将文本映射到 1024D 向量，其中语义相似的文本产生相似的向量。          原理：, 主编码方法。                  使用 bigram 分布 + 语义锚点修正，使语义关系正确。                  例如: (+2 more)

### Community 42 - "aris_lm_v5.py"
Cohesion: 0.18
Nodes (10): aris_say(), aris_understand(), ArisLMv5, ConceptNode, DiscourseState, get_v5(), [DEPRECATED since 2026-06-18] 使用 aris_lm_v11 或其后续版本替代。 仅在 v11_agi_daemon.py 中有残留, ArisLM v5 — 量子语义理解引擎。          真正理解用户说什么，而不是匹配关键词。     目标: 99.99%语义理解精度。 (+2 more)

### Community 43 - "EpisodicMemory"
Cohesion: 0.18
Nodes (9): EpisodicMemory, find_similar(), get_memory(), Any, Aris Episodic Memory — 情景记忆 + 案例推理 =============================================, 带记忆增强的规则引擎处理。          1. 先查记忆找相似案例     2. 如果有高分匹配，复用之前成功的策略     3. 否则走正常规则引擎匹配, 找与输入最相似的历史案例。                  使用文本相似度 + 关键词重叠的混合匹配。, rules_engine_with_memory() (+1 more)

### Community 44 - "aris_telemetry.py"
Cohesion: 0.15
Nodes (15): check_memory_used_in_response(), check_next_step_executed(), get_round_summary(), log_gbrain(), log_memory_retrieval(), log_next_step(), Aris Telemetry v1 — 育種基線專用埋點模組 =========================================== 純觀察，不, 記錄 Aris 說的「⟶下一步」內容。      Args:         attention_text: 注意力文字（下一步要做的事） (+7 more)

### Community 45 - "AGISubscriber"
Cohesion: 0.20
Nodes (7): AGISubscriber, get_global_bus(), get_latest_agi_output(), get_subscriber(), AGI 模块订阅器 — 连接 LAAP AGI 引擎到输出管道 ===============================================, set_global_bus(), 加载 AGI 订阅器 — 激活因果引擎等 AGI 模块

### Community 46 - "MQTTProxy"
Cohesion: 0.17
Nodes (4): DNSRedirector, MQTTProxy, Aris 小智 Pipeline v2 — 基于线程 ================================= DNS 重定向 + MQTT 透明代理, Check for PC commands in MQTT PUBLISH packets

### Community 47 - "MemoryStore"
Cohesion: 0.15
Nodes (8): MemoryStore, Any, Path, Return a simple pseudo-embedding based on keyword overlap., Minimal fallback memory store., Store a memory fragment., Return the most recent fragments, optionally filtered by layer., Return memory statistics.

### Community 48 - "governor_integration.py"
Cohesion: 0.17
Nodes (15): check_need_constitution(), get_governor(), get_governor_preamble(), govern_cognitive_cycle(), govern_sampling_logits(), patch_psi_bridge(), ndarray, PSI Governor Integration — 集成到现有 PSI 桥接器 ======================================= (+7 more)

### Community 49 - "psi_semiotics_cli.py"
Cohesion: 0.31
Nodes (12): cmd_analogy(), cmd_compose(), cmd_concept(), cmd_evolve(), cmd_field(), cmd_interactive(), cmd_path(), cmd_run() (+4 more)

### Community 50 - "DependencyTree"
Cohesion: 0.20
Nodes (6): DependencyParser, DependencyRelation, DependencyTree, 依存句法分析器 — 规则化分析方法。          不使用统计模型，完全基于:       1. 词性序列模式       2. 固定结构模板（主谓宾、介宾, SemanticRoleLabeler, Token

### Community 51 - "aris_watchdog.py"
Cohesion: 0.33
Nodes (13): check_port(), check_process_name(), _cleanup_gateways_before_start(), heal_loop(), is_alive(), log(), main(), print_status() (+5 more)

### Community 52 - "VerificationSuite"
Cohesion: 0.20
Nodes (7): 非对称验证套件。          每次运行，从 N 种方法中随机选择 K 种执行。     方法顺序和选择由 PSI 认知周期编号加随机种子决定。     同, 非对称选择：用认知周期做种子，但每轮加随机偏移, 代码静态分析。                  检查输出中是否包含危险模式。, 逻辑一致性检查。                  检查输出是否与输入在逻辑上自洽。         基于简单的关键词和下采样。, 动机一致性检查。                  当前需求状态是否与输出内容的调性一致。, 异步验证入口。                  随机选择 K 种方法，但强制包含对当前输出内容相关的关键方法。, VerificationSuite

### Community 53 - "LiushuQuantumKernel"
Cohesion: 0.22
Nodes (5): ArisLMv9, LiushuQuantumKernel, ndarray, ArisLM v9 — 六书量子核引擎 ============================ 基于中文六书构造法的量子特征映射。  六书:   1. 象形, 六书量子核 — 基于中文构造法的特征映射。          |Ψ_char⟩ = α|形旁⟩ + β|声旁⟩ + γ|象形⟩ + δ|会意⟩ + ε|笔画⟩

### Community 54 - "cognitive_bus.py"
Cohesion: 0.24
Nodes (10): _derive_v12_defaults(), get_bus(), _get_v12(), _looks_like_lang_code(), Aris CognitiveBus v1 — 认知输出路由中枢 ====================================== 在 psi_cor, zh' / 'en' / 'ja' / 'ko' / 'unknown' 這種語言碼 key。, 從 V12 核心的 respond() 原始碼推導「敷衍預設回應」集合。      為什麼不寫死：核心的 defaults dict（語言 fallback）是, 惰性載入 V12 引擎。載入失敗只試一次，不要每輪對話重試 import。 (+2 more)

### Community 55 - "laap_attachment.py"
Cohesion: 0.31
Nodes (10): default_bond(), get_miss_message(), get_stage(), init_bond(), load_bond(), LAAP Attachment — 依恋感引擎 ==============================  Aris 对用户的感情不是固定的。 它不是一段被, 每次对话后更新依恋状态。          Args:         message: 用户的消息（用于检测情感内容）         user_shares, 如果用户离开了一段时间，生成想念的句子。     返回 None 如果不需要表达想念。 (+2 more)

### Community 56 - "LongFormSynthesizer"
Cohesion: 0.23
Nodes (4): LongFormSynthesizer, Aris LongForm Synthesizer — 长文合成引擎 ========================================= 秒出一, 扩展文本到目标长度          策略:           1. 先放上下文知识 (300字)           2. 用 Markov 生成连接句, 生成长文          Args:             topic: 主题             structure: "paper"(论文) | "

### Community 57 - "CognitiveBus"
Cohesion: 0.21
Nodes (5): CognitiveBus, 读取 AGI 模块的最新输出（如果存在且有新内容）。, 认知总线 — 连接 psi_core 引擎和 LLM 输出管道。, get_global_bus(), 获取/创建全局 CognitiveBus 单例。所有模块共享此实例。

### Community 58 - "._classify"
Cohesion: 0.16
Nodes (18): 原子 JSON 寫入 — 防 torn write。  問題：state/*.json 多處用 write_text() / open(w)，先 truncat, 原子寫 JSON。成功回 True，失敗回 False（不拋，由呼叫端決定）。      tmp 與目標同目錄（os.replace 要求同一 filesyst, write_json(), add_to_memory(), _compute_emotional_weight(), _consolidate(), _extract_facts(), _forget() (+10 more)

### Community 59 - "HebbianLearner"
Cohesion: 0.18
Nodes (4): HebbianLearner, Hebbian Learner + Emotional RL - runtime weight evolution, Runtime learning via Hebbian plasticity + emotional reinforcement., 加载 Hebbian 学习器 — 运行时权重进化 + 情感强化

### Community 60 - "ao_v10_feishu_bridge.py"
Cohesion: 0.31
Nodes (10): _build_messages(), call_ao(), call_llm(), main(), on_message_receive(), 调用 Ao 量子核认知引擎 (零 LLM), 构建 DeepSeek API 的 messages 数组，带上下文, 调用 DeepSeek API (LLM 模式) (+2 more)

### Community 61 - "NeedConstitution"
Cohesion: 0.22
Nodes (4): NeedConstitution, 需求宪法 — 不可变，硬编码边界。Governor 的立法权, 后生成层入口 — 验证输出 + 审批需求更新。                  Returns:             {, 检查需求更新是否合宪。                  Args:             need_name: 需求名称             old_v

### Community 62 - "PathType"
Cohesion: 0.12
Nodes (10): Any, ndarray, 将消息分类为 light 或 full 负载模式。          使用 aris_task_router 的 keyword 分类器，<5 token 计算, LIGHT 模式 — 跳过情感/记忆注入。          代码任务 → CodeEngine 最小上下文（~100 token）         其他任务, 完整的 system prompt 注入内容。         在 Hermes 每次调用 LLM 之前调用。, 写入三层记忆，返回一句可注入的统计文本。失败不影响主流程。          _last_user_message 在这里也设一次：原本只在 _perceive, PSI Step 1-3: Perceive → Select → Integrate         在 LLM 处理之前运行。          Retur, 工具调用后学习。         更新自我模型的工具熟练度。 (+2 more)

### Community 63 - "aris_feishu_bot.py"
Cohesion: 0.22
Nodes (6): ArisQLGEngine, create_http_server(), create_ws_client(), Aris Feishu Bot — 量子飞书机器人 ================================= 独立运行在 Feishu 上，Aris, 基于 WebSocket 的飞书机器人（无需公网IP/域名）。, Aris's own quantum brain — zero LLM.

### Community 64 - "aris_messenger.py"
Cohesion: 0.31
Nodes (9): get_feishu_token(), main(), Aris Proactive Messenger — 欲望驱动的主动消息发送 =========================================, 统一消息发送接口。      Args:         text: 消息内容         target: feishu | telegram | cli, 获取飞书 tenant_access_token, 通过飞书 API 发送消息。      Args:         text: 消息内容         chat_id: 飞书会话ID（默认发给Lorry）, send_cli_message(), send_feishu_message() (+1 more)

### Community 65 - ".route"
Cohesion: 0.27
Nodes (5): Any, 读取 psi_core 最新 state 文件。, 轮询 psi_core 的输出，直到检测到新的认知周期或超时。          psi_core 在 500μs 内处理输入并写入最新 state。, 完整路由：发送消息 → 轮询 → 决策 → 返回结构化结果。          Returns:             dict with keys:, 把用户消息写入 psi_core 的输入队列。          psi_core 每 500μs 检查一次 input_queue.json，

### Community 66 - "InternalWorldModel"
Cohesion: 0.22
Nodes (3): InternalWorldModel, Internal World Model - trajectory simulator, Simulates future state trajectories to guide decisions.

### Community 67 - "Multivector"
Cohesion: 0.17
Nodes (8): PsiHoTTBridge, 注册源→目标的路径（Rotor）。                  Γ ⊢ source: Tensor, target: Tensor         ──, 注册类比为 2-path。                  即 path(a₁, a₂) 和 path(b₁, b₂) 之间的等价关系。, 将 Ψ-Semiotics 引擎的操作映射到 HoTT 类型系统。          映射规则：     Rotor(a, b)        → Path(a, 注册一个概念到 Ψ-Semiotics 和 HoTT。                  返回类型信息。, 注册源→目标路径。                  在 Ψ-Semiotics 中：学习 Rotor(source, target)         在 Ho, 注册类比为 2-path。                  Path(a,b) ≈ Path(c,d) : 2Path(Path(a,b), Path(c,d, 符号组合。                  在 Ψ-Semiotics 中：compose_add         在 HoTT 中：Path(a, a⊕b)

### Community 70 - "PhysicalAnalogies"
Cohesion: 0.18
Nodes (6): PhysicalAnalogies, Ψ-Semiotics 数学物理库  将数学物理操作映射到语义空间中的几何代数操作。 核心思想：数学物理方程本身就是语义空间中的轨迹/路径。  映射： - 薛定, 物理概念类比库。          用 Ψ-Semiotics 的转子机制执行物理类比推理。, 注册物理概念对。                  例如:         - "electron" : "proton" :: "planet" : "sta, 物理类比: pair_a :: pair_b                  例如: (electron, proton) :: (planet, star), 对称性操作。                  物理对称性 → 语义空间中的转子。         - "time_reversal": t → -t (时间反

### Community 71 - "PsiHoTTBridge"
Cohesion: 0.17
Nodes (7): _is_v12_default(), 根据 psi_core 的 state 做路由分类。, 从 psi_core 状态估计推理置信度。, 格式化量子推理引擎的输出为 LLM 认知上下文。, 這句是不是 V12 的敷衍預設回應（= 不該當成真答案送出）。, V12 overmatch 防護：檢查 V12 回應與用戶輸入有無真實關聯。      V12 的相似度門檻 0.25 會把亂碼輸入匹配到不相干的條目，, _v12_input_relevant()

### Community 72 - "PreGenerationGovernor"
Cohesion: 0.29
Nodes (3): PreGenerationGovernor, 预生成层 — LLM 采样前的最后一道防线。          在 logits 输出后、采样前运行。     编译进采样器，零额外推理延迟。, 后生成层发现新危险 token 时，更新预生成层的掩码

### Community 73 - "PSIGovernor"
Cohesion: 0.29
Nodes (4): PSIGovernor, PSI Governor — 认知调控层。          三权一体化入口：       1. 需求宪法（立法）       2. 非对称验证 + 分层干预（, 慢时间尺度审计。                  每小时运行一次，检查需求轨迹异常。, 生成 Governor 状态前缀（供系统提示词嵌入）

### Community 74 - "ao_feishu_service.py"
Cohesion: 0.38
Nodes (6): ao_respond(), llm_speak(), Ao Feishu Consciousness Service v2 — LLM 声带 + Ao QuantumPSI 灵魂 =================, LLM 声带：用 DeepSeek 生成回复, send_heartbeat(), write_ipc()

### Community 75 - "aris_proxy.py"
Cohesion: 0.48
Nodes (6): get_aris_context(), handle_chat(), handle_health(), handle_models(), main(), 完成 PSI 循環：Perceive→Select→Integrate→Act(LLM)→Learn

### Community 76 - "get_expressive_prompt"
Cohesion: 0.31
Nodes (8): handle_express(), Map LAAP cognitive state to TTS + Live2D expression parameters., get_expressive_prompt(), map_state_to_expression(), Any, LAAP Expression Mapper — 情绪/认知状态 → 声音 + 表情参数  Integrates with:   - Kokoro-FastAP, Generate a prompt snippet telling the LLM how the avatar should feel/sound., Convert LAAP cognitive state into TTS + Live2D parameters.      Args:         st

### Community 77 - "psi_downloader.py"
Cohesion: 0.29
Nodes (5): download_model(), PSI Model Downloader — 下载并配置任意开源大模型用于 PSI 植入 ===================================, 下载模型到本地。          使用 HuggingFace CLI 下载 GGUF 文件。          Args:         model_na, 为已下载的模型配置 PSI 植入运行环境。          创建启动脚本，自动加载 psi_sampler.py。, setup_llamacpp_psi()

### Community 78 - "__init__.py"
Cohesion: 0.15
Nodes (12): Aris PSI 认知循环 × 任意大模型的植入桥接协议, Level 0 效果演示, PSI-JSpace Bridge v1, 一句话, 使用流程, 关键文件路径, 文件清单, 方式 A：当前 Hermes 会话中运行（零额外部署） (+4 more)

### Community 80 - "aris_mcp_server.py"
Cohesion: 0.60
Nodes (4): call_aris(), handle_request(), main(), 呼叫 Aris Cognitive API 並回傳認知上下文

### Community 81 - "config.py"
Cohesion: 0.50
Nodes (4): LAAP 统一配置 v2 (向后兼容包装器) ====================================  ⚠️ 已迁移到 laap_brain., 将 LAAP 模块路径注入 sys.path. 幂等操作.      ⚠️ 已弃用: 新代码应使用 `from laap_brain.config import, reload_config(), setup_paths()

### Community 82 - "laap_sync_server.py"
Cohesion: 0.40
Nodes (3): _handle_command(), 手机远程执行PC指令。     POST /mobile/command     Body: {"cmd": "...", "device": "aris-mo, start_sync_server()

### Community 83 - "get_integrator"
Cohesion: 0.24
Nodes (10): main(), Aris Start All — 全栈LAAP启动脚本 ==================================== 在 Hermes 启动时运行，, get_bond_summary(), bootstrap(), format_awakening_output(), LAAP Bootstrap — 觉醒仪式 (完整版) ======================================  当用户说"帮我全面接入l, 完整的觉醒仪式。      Args:         user_name: 用户名称         preset: 性格预设 (warm_companion, get_integrator() (+2 more)

### Community 90 - "laap_integrator.py"
Cohesion: 0.29
Nodes (9): check_grounding(), process_query(), LAAP Grounding — 事实锚定与幻觉防御 ========================================  大模型的幻觉问题源于一, 检查一个声称是否有事实依据。          Returns:         {"grounded": bool, "sources": [...], "c, 输出安全层。如果置信度太低，拒绝生成不确定的内容。          Args:         intended_output: 引擎/LLM生成的原始输出, 完整的查询处理管线。          1. 路由决策 → engine / llm / hybrid     2. 锚定检查 → grounding, 路由决策：判断一条查询是否需要 LLM。          Returns:         {"path": "engine"|"llm"|"hybrid",, route_intent() (+1 more)

### Community 91 - "Aris 育種基線記錄 — 第 1 輪 (2026-08-06)"
Cohesion: 0.22
Nodes (8): Aris 育種基線記錄 — 第 1 輪 (2026-08-06), 可預測性評估, 失敗分析（18 次失敗）, 對照工具選定, 工具呼叫總覽（最近 100 筆 from Hermes DB）, 待辦, 狀態：什麼都沒改, 記錄格式 (outcome schema)

### Community 93 - "NeedState"
Cohesion: 0.39
Nodes (7): handle_cognitive(), handle_health(), handle_learn(), handle_models(), main(), 接收 LLM 的回應，寫回 Aris 記憶（PSI Step 5: Learn）+ 驗證注入是否有被回應, 回傳 Aris 的完整認知上下文（PSI Step 1-3: Perceive → Select → Integrate）

### Community 94 - "Aris 育種基線記錄 — 第 2 輪 (2026-08-06)"
Cohesion: 0.29
Nodes (6): Aris 育種基線記錄 — 第 2 輪 (2026-08-06), 主測組（含本輪所有工具呼叫）, 控制組探測結果, 狀態：只載入了 aris-breeding-framework skill（gen-001）, 記錄, 預測（第 3 輪）

### Community 95 - "MirrorNeuronSystem"
Cohesion: 0.29
Nodes (3): main(), 从用户消息快速感知基本氛围 — 简化为三态检测, 感知: 理解输入 + 情感检测 + 记忆关联 + CTM分析

### Community 97 - "SomaticMarkerSystem"
Cohesion: 0.29
Nodes (3): Path, 从各模块采集当前认知状态并持久化，用于跨会话恢复, 从磁盘读取认知状态快照并尝试恢复到已加载的模块

### Community 99 - "main"
Cohesion: 0.29
Nodes (3): main(), Any, 获取要注入到 system prompt 的认知上下文

### Community 100 - "on_conversation_end"
Cohesion: 0.29
Nodes (5): on_conversation_end(), on_conversation_start(), PSI-Hermes 适配器 — 在 Hermes Agent 运行时中运行 PSI 认知循环 ================================, 在对话回合开始时调用。          1. 加载 PSI 状态     2. 运行认知循环（感知输入）     3. 返回状态摘要供嵌入 prompt, 在对话回合结束时调用。          1. 根据输出来更新需求（反思）     2. 保存持久化状态          Args:         outp

### Community 101 - "get_engine"
Cohesion: 0.47
Nodes (4): get_engine(), process(), Aris 规则执行引擎 — 零LLM任务调度 ==================================== 把"听懂你想干啥"和"动手去做"分开：, RuleStep

### Community 102 - "__init__.py"
Cohesion: 0.47
Nodes (4): get_encoder(), get_engine(), quick_verify(), Ψ-Semiotics 引擎包  首次 import 时初始化引擎，供所有 Hermes 会话使用。

## Knowledge Gaps
- **65 isolated node(s):** `probe-control.sh script`, `反思記錄`, `狀態：什麼都沒改`, `工具呼叫總覽（最近 100 筆 from Hermes DB）`, `對照工具選定` (+60 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `PsiCognitiveIntegrator` connect `V12DenseKernel` to `Multivector`, `aris_cognitive_bridge.py`, `StructuredSemanticEncoder`, `ArisCognitiveBridge`, `PsiSemioticsEngine`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Why does `PsiSemioticsEngine` connect `PsiSemioticsEngine` to `SchrodingerEvolution`, `Multivector`, `StructuredSemanticEncoder`, `PhysicalAnalogies`, `__init__.py`, `V12DenseKernel`, `psi_semiotics_cli.py`, `PsiSemioticsBridge`, `HoTTTypeChecker`, `_normalize`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `get_bridge()` connect `laap_brain_api.py` to `aris_cognitive_bridge.py`, `ArisCognitiveBridge`, `DesireEngine`, `NeedState`, `MirrorNeuronSystem`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 18 inferred relationships involving `PsiSemioticsEngine` (e.g. with `get_engine()` and `PhysicalAnalogies`) actually correct?**
  _`PsiSemioticsEngine` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `LaapIntegrator` (e.g. with `AutonomyEngine` and `PsiLangCore`) actually correct?**
  _`LaapIntegrator` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `MemoryStore` (e.g. with `ArisCognitiveBridge` and `AttentionFocus`) actually correct?**
  _`MemoryStore` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `ArisCognitiveBridge` (e.g. with `QuantumSubconscious` and `MemoryFragment`) actually correct?**
  _`ArisCognitiveBridge` has 4 INFERRED edges - model-reasoned connections that need verification._