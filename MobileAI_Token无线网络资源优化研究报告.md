# 面向Mobile AI/Token业务的无线网络资源分配优化研究报告

## 一、云服务器侧AI推理的计算调度热点与瓶颈

### 1.1 Prefill-Decode两阶段异构特性——LLM推理的核心矛盾

LLM推理请求在GPU上经历两个截然不同的阶段：

| 阶段 | 计算特性 | 硬件瓶颈 | 控制指标 |
|------|----------|----------|----------|
| **Prefill** (预填充) | 处理整个输入prompt，生成KV Cache，大量矩阵乘法并行 | **计算密集型** (Compute-bound)，GPU算力满载 | **TTFT** (Time To First Token) |
| **Decode** (解码) | 逐token自回归生成，小矩阵-向量乘法，频繁读KV Cache | **内存带宽密集型** (Memory-bandwidth-bound)，GPU计算核心空闲 | **TPOT** (Time Per Output Token) |

**核心矛盾**：Prefill需要原始算力，Decode需要内存带宽。将两者放在同一GPU上运行意味着两者都无法获得真正需要的资源。

**量化影响**：在数百到数千并发用户场景下，这种冲突成为瓶颈。Prefill作业排队等待Decode批次，TTFT膨胀；Decode共享GPU计算但无法高效使用。更多GPU意味着更高的cost-per-token，延迟仍然高。

（来源：UCSD Hao AI Lab, DistServe/Sarathi-Serve系列研究；TaiChi, arxiv 2508.01989, 华为云/中山大学/港中大联合发表）

### 1.2 PD Aggregation vs PD Disaggregation——架构之争

**PD Aggregation** (如Orca, Sarathi-Serve)：Prefill和Decode在同一GPU实例上共存。
- 优点：资源利用率高，所有实例参与prefill → **TTFT低**
- 缺点：prefill/decode互相干扰 → **TPOT劣化**

**PD Disaggregation** (如Splitwise, DistServe, llm-d)：Prefill和Decode物理分离到不同GPU。
- 优点：无干扰，独立扩展 → **TPOT优**
- 缺点：仅部分实例处理prefill → **TTFT劣化**

**TaiChi系统的核心发现**（华为云/中山大学/港中大，2025）：
- PD Aggregation在TTFT约束紧、TPOT宽松时最优
- PD Disaggregation在TPOT约束紧、TTFT宽松时最优
- **但在TTFT和TPOT都需满足的平衡场景下，两种方案都无法达到最优goodput**
- TaiChi提出统一架构，goodput提升高达77%

（来源：TaiChi论文, arxiv 2508.01989）

### 1.3 KV Cache传输——Disaggregated Inference的通信瓶颈

Prefill完成后需要将KV Cache（对长上下文模型可达数GB）传输到Decode实例。

**当前解决方案**：
- **NIXL** (NVIDIA Inference Xfer Library)：vendor-agnostic数据传输库，底层使用RDMA (InfiniBand/RoCE)，GPU-to-GPU直接内存传输，无需CPU/OS参与
- **llm-d** (CNCF Sandbox项目，Red Hat/Google/NVIDIA/AMD等支持)：Kubernetes原生分布式推理框架，Prefill和Decode作为独立Pod，通过HPA独立扩展

**关键性能数据**：
- KV Cache传输延迟相比prefill计算时间可忽略不计
- 分层KV Cache架构：GPU HBM → CPU DRAM → 本地SSD → 远程存储
- 标准GPU-only部署在HBM饱和后性能急剧下降；存储支持的配置可维持性能

（来源：llm-d项目, Medium文章 "Disaggregated LLM Inference", 2026年3月）

### 1.4 多用户并发下的GPU调度瓶颈

**Continuous Batching** (连续批处理)：LLM serving的核心优化，允许不同请求在decode阶段共享GPU。但当前面临：

| 瓶颈 | 描述 |
|------|------|
| **请求级SLO异构** | 不同应用的TTFT/TPOT要求差异巨大：chat需要低TTFT，streaming需要稳定TPOT |
| **GPU multitasking限制** | LLM推理的GPU multitasking仍面临挑战（arxiv 2508.08448） |
| **KV Cache内存爆炸** | 并发用户增多时KV Cache占用线性增长，HBM成为硬约束 |
| **Prefill队列拥塞** | 高并发时prefill请求排队导致TTFT急剧恶化 |

### 1.5 云-边-端协同的调度挑战

**边缘推理的兴起**：
- 实时AI场景（视频理解、WebRTC音频）需要低延迟，边缘部署可将RTT从百毫秒级降至个位数毫秒
- 但边缘GPU资源有限，需要与云端协同调度

**当前研究热点**：
- Task offloading：任务在端-边-云间的动态卸载（多篇论文发表于Springer/Nature 2025-2026）
- Multi-objective optimization：同时优化延迟、能耗、QoE
- Deep reinforcement learning for scheduling：用DRL做动态任务调度

（来源：Springer Journal on Wireless Communications and Networking, 2025; Nature Scientific Reports, 2025; ScienceDirect, 2024）

---

## 二、从云计算瓶颈导出的无线网络机会点

### 机会1：TTFT/TPOT感知的无线资源调度

**云计算问题**：TTFT和TPOT是LLM serving的两个核心SLO，但当前无线网络完全不感知这两个指标。

**无线网络机会**：

| 阶段 | 网络需求 | 调度策略 |
|------|----------|----------|
| **Prefill阶段** (用户发送prompt) | 大块上行数据一次性传输，需要**低延迟、高吞吐** | 为prefill上行分配高优先级、大grant，避免排队 |
| **TTFT等待** (服务端计算) | 网络空闲，可调度其他用户 | 利用TTFT窗口调度其他用户的UL/DL |
| **Decode阶段** (token streaming下行) | 周期性小包下行，需要**稳定、低jitter** | 为decode下行预留持续资源，避免调度间隔波动 |
| **TPOT约束** | 每个token间隔需<阈值(如50ms) | 保证token streaming的调度周期稳定 |

**具体技术方案**：

**方案A：AI-traffic-aware Scheduler**
- 无线网络识别AI推理流量（基于DPI或token streaming特征）
- Prefill上行触发时临时提升调度优先级（类似URLLC的preemption机制）
- Decode下行配置半持续调度(SPS)，减少每token的调度开销

**方案B：Prefill-Decode分离调度**
- 对应云侧PD disaggregation架构
- Prefill上行和Decode下行使用不同的QoS流/切片
- Prefill上行：burst-aware调度，容忍突发
- Decode下行：periodic-aware调度，保证token pacing

### 机会2：AI上行低延迟传输机制

**云计算问题**：实时AI场景（视频理解、多模态分析）需要周期性大量上行数据。SA4#136测试显示：实时视频理解UL/DL=5-6x，每500ms上传一帧图像。

**无线网络机会**：

| 方案 | 原理 | 适用场景 |
|------|------|----------|
| **Multi-bit SR** | SR携带buffer状态信息，gNB可直接分配合适大小grant，跳过BSR步骤 | 所有AI上行场景 |
| **CB-PUSCH for BSR** | 在contension-based资源上直接发送BSR，减少SR→grant→BSR→grant→data的多round-trip | 小包AI反馈（工具调用结果、状态报告） |
| **Preconfigured Grant for AI** | 为周期性AI上行（如每500ms的视频帧）配置semi-persistent UL资源 | 视频理解、实时音频 |
| **Early BSR triggering** | 收到NACK时立即触发BSR，帮助网络调度重传资源 | HARQ失败后的快速恢复 |

（依据：RAN1#125 10.5.5讨论，R1-2603513 MediaTek, R1-2604705 Qualcomm, R1-2604065 LG等）

### 机会3：Token-native网络传输——从HTTP SSE到RTP-like

**云计算问题**：当前AI token通过HTTP SSE传输，存在大量chunked streaming开销。华为SA4文稿证实：token chunk pacing比网络RTT快1000倍（0.116ms vs 63ms），说明choking在服务端而非网络。

**无线网络机会**：

**现状问题**：
- HTTP SSE的chunked传输在无线侧产生大量小包，调度效率低
- 每个chunk独立TCP连接开销
- 无线网络无法区分"token chunk"和"普通HTTP data"

**技术方案**：

| 方向 | 描述 |
|------|------|
| **RTP-like token传输** | 将token流封装在RTP包中，每个token或token batch一个RTP包；无线网络可基于RTP序列号做token-aware调度 |
| **Token QoS标记** | 在PDCP/SDAP层增加token类型标记（文本/视觉/音频），无线网络据此差异化调度 |
| **Token pacing协调** | 网络告知服务端当前无线信道容量，服务端据此调整token生成/发送速率，避免buffer溢出 |

（依据：SA4#136 S4-261051 Huawei "AI tokenized traffic further documentation"）

### 机会4：边缘推理与无线调度联合优化

**云计算问题**：Prefill计算密集但可预测（取决于prompt长度）；Decode计算轻但实时性要求高。边缘GPU资源有限。

**无线网络机会**：

| 方案 | 描述 |
|------|------|
| **Prefill offloading to edge** | 将prefill阶段卸载到边缘MEC（计算密集但无实时性要求），decode在云端；无线网络负责prefill数据的低延迟上行传输 |
| **Edge-cloud decode协作** | Decode阶段的KV Cache在边缘和云端之间同步；无线网络为KV Cache传输分配高优先级低延迟通道 |
| **AI task-aware切片** | 为AI推理流量创建专用网络切片，与普通数据流量隔离；切片内进一步区分prefill(高带宽)和decode(低延迟稳定) |
| **Predictive resource reservation** | 基于AI请求的prompt长度预测prefill计算时间和decode时长，提前预留无线资源 |

### 机会5：多用户AI并发的无线资源公平性

**云计算问题**：大量用户并发访问AI服务时，GPU资源竞争导致部分用户TTFT/TPOT恶化。

**无线网络机会**：

| 方案 | 描述 |
|------|------|
| **Token-rate-based scheduling** | 以用户实际token消费速率（而非传统吞吐量）作为调度权重；高token消耗用户获得更多资源 |
| **TTFT-aware preemption** | 当某用户TTFT即将超SLO时，无线网络可preempt其他用户的资源（类似URLLC eMBB preemption） |
| **Fair token sharing** | 在无线侧实现token消费的公平性保障，避免"饥饿"用户 |
| **Adaptive MCS for AI traffic** | AI streaming traffic对jitter敏感但对瞬时吞吐不敏感；可使用更高阶MCS+更多HARQ重传来降低调度频率 |

### 机会6：AI KV Cache的网络级缓存与预取

**云计算问题**：KV Cache是LLM推理的核心资产。llm-d实现了分层KV Cache (GPU→CPU→SSD→远程存储)，但网络传输仍是瓶颈。

**无线网络机会**：

| 方案 | 描述 |
|------|------|
| **网络级KV Cache缓存** | 在无线网络的边缘节点缓存高频用户的KV Cache片段；相同前缀的prompt可直接命中缓存，跳过prefill |
| **Prefix-aware调度** | 识别具有相同前缀的AI请求（如相同system prompt），将它们调度到已缓存对应KV Cache的边缘节点 |
| **Proactive KV Cache预取** | 基于用户历史AI使用模式，预测下一个请求的可能prompt前缀，提前在边缘预取KV Cache |

---

## 三、技术研究路线图

### Phase 1：基础机制（6-12个月）

| 研究方向 | 关键问题 | 预期产出 |
|----------|----------|----------|
| AI traffic detection | 如何在无线侧识别AI token流量 | AI-traffic-aware调度器原型 |
| TTFT/TPOT as QoS metric | 如何将TTFT/TPOT映射到无线QoS参数 | AI QoS framework |
| Multi-bit SR for AI | SR如何携带AI上行信息 | SR增强方案提案 |

### Phase 2：系统集成（12-24个月）

| 研究方向 | 关键问题 | 预期产出 |
|----------|----------|----------|
| PD disaggregation网络支持 | Prefill/Decode分离后网络如何协同 | 端到端PD-aware调度 |
| Edge-cloud AI协同 | 边缘推理与无线调度联合优化 | 联合优化算法 |
| Token-native传输 | RTP-like token传输协议设计 | 协议原型 |

### Phase 3：智能优化（24-36个月）

| 研究方向 | 关键问题 | 预期产出 |
|----------|----------|----------|
| KV Cache网络级管理 | 缓存/预取/同步机制 | 智能KV Cache管理 |
| DRL-based resource allocation | 基于强化学习的无线资源动态分配 | 自适应调度系统 |
| End-to-end AI QoE | 端到端QoE建模与优化 | AI QoE标准提案 |

---

## 四、参考来源

1. TaiChi论文, "Prefill-Decode Aggregation or Disaggregation? Unifying Both for Goodput-Optimized LLM Serving", arxiv 2508.01989, 华为云/中山大学/港中大, 2025
2. DistServe, "Throughput is Not All You Need: Maximizing Goodput in LLM Serving", UCSD Hao AI Lab
3. Splitwise/PD Disaggregation系列研究, Patel et al., 2024
4. llm-d, CNCF Sandbox项目, Red Hat/Google/NVIDIA/AMD等, https://github.com/llm-d/llm-d
5. "Disaggregated LLM Inference: How Splitting Prefill and Decode Changes Everything", Medium, 2026年3月
6. "Towards Efficient and Practical GPU Multitasking in the Era of LLM", arxiv 2508.08448
7. 3GPP SA4#136 S4-260961/260963, Qualcomm Japan, AI Traffic Characteristics
8. 3GPP SA4#136 S4-261049/261051/261143, Huawei, Tokenized Traffic
9. 3GPP RAN1#125 10.5.5, Multi-bit SR与CB-BSR讨论 (R1-2603513/2603865/2604705/2604065)
10. "A survey on resource scheduling approaches in multi-access edge computing", Cluster Computing, Springer, 2024
11. "Dynamic task scheduling in wireless edge computing using deep reinforcement learning", Springer, 2025
12. "Joint optimization of multi-dimensional resource allocation and task offloading for QoE enhancement", ScienceDirect, 2024
