---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<h1>&#128075; About Me</h1>

I am a Ph.D. student at Southern University of Science and Technology (SUSTech), supervised by <a class="external-link" href="https://scholar.google.com/citations?user=r9ezy2gAAAAJ&hl=en">Zhenkun Wang</a>, working on AI for Optimization, specifically Neural Combinatorial Optimization (NCO). 

**Neural Combinatorial Optimization (NCO)** studies how neural networks can learn to solve discrete optimization problems such as routing, scheduling, and assignment. Instead of designing every search rule by hand, NCO learns policies from data and interaction, aiming to produce fast solvers that can generalize across problem scales, distributions and complex problems with diverse constraints.

My research focuses on deep reinforcement learning for vehicle routing problems (VRPs), with an emphasis on **out-of-distribution zero-shot generalization**. My recent first/co-first-author work includes the following: **(1) ICAM**, an instance-conditioned adaptation model for generalization to **thousand-scale** VRP instances; **(2) L2R**, a neural routing solver scalable to **10-million-node** instances; and **(3) URS**, a generalist neural solver covering **over 100** VRP variants.

As of June 15, 2026, I have published **11 papers**, including **4 first/co-first-author papers**. My work has appeared in venues including **ICML**, **KDD**, and **IEEE T-ITS**. For more details, please see my <a class="external-link" href="cv/zhoucl_CV_English.pdf">English CV</a> and <a class="external-link" href="cv/zhoucl_CV_Chinese.pdf">Chinese CV</a>.


<!-- As of June 15, 2026, I have published **11 papers**, including **4 first/co-first-author papers**. My work has appeared in venues including **ICML**, **KDD**, and **IEEE T-ITS**, with <a class="external-link" href='https://scholar.google.com/citations?user=9IzIC7kAAAAJ&hl=en'>Google Scholar citations <strong><span id='total_cit'>256</span></strong></a> <a href='https://scholar.google.com/citations?user=9IzIC7kAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ gsShieldUrl | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. -->

<div class="notice--info opportunity-notice">
  <strong>&#x1F4E2; I'm on the job market! Let's connect.</strong> &#x1F52D; I am approaching graduation and actively seeking postdoctoral positions or related industry research roles. 
  <br>
  &#x1F91D; If my work aligns with your interests, please feel free to contact me: <a class="external-link" href="mailto:zhoucl2022@mail.sustech.edu.cn">zhoucl2022@mail.sustech.edu.cn</a>.
</div>

<span class='anchor' id='news'></span>

<h1>&#128293; News</h1>
- 🎉 *05/2026*: L2R appeared at the 32nd SIGKDD Conference on Knowledge Discovery and Data Mining (KDD).
- 🎉 *05/2026*: URS appeared at the 43rd International Conference on Machine Learning (ICML).
- 🎉 *03/2026*: ICAM appeared in IEEE Transactions on Intelligent Transportation Systems (T-ITS).
<!-- - *2025*: 🚀 Started leading EasyCO, a learning-driven platform for combinatorial optimization. -->
- 🎓 *09/2022*: Began Ph.D. study at Southern University of Science and Technology.

<span class='anchor' id='research-highlights'></span>

<h1>&#127919; Research Highlights</h1>

<div class="highlight-paper-card">
  <div class="highlight-paper-image">
    <img src="images/papers/ICAM.png" alt="ICAM overview">
  </div>
  <div class="highlight-paper-body">
    <h3>ICAM: Instance-Conditioned Adaptation Model for Thousand-Scale Generalization</h3>
    <p><span class="venue-badge">T-ITS 2026</span></p>
    <p class="badge-row">
      <a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2405.01906">&#128196; Paper</a>
      <a class="readme-badge code-badge" href="https://github.com/CIAM-Group/ICAM">&#128187; Code</a>
    </p>
    <ul>
      <li>Introduced a lightweight instance-conditioned adaptation function and a low-complexity attention mechanism to adjust policies using instance-specific information.</li>
      <li>Validated the method on four representative routing problems, TSP, CVRP, ATSP, and CVRPTW, improving generalization while preserving fast inference.</li>
    </ul>
  </div>
</div>

<div class="highlight-paper-card">
  <div class="highlight-paper-image">
    <img src="images/papers/L2R.png" alt="L2R overview">
  </div>
  <div class="highlight-paper-body">
    <h3>L2R: Learning to Reduce Search Space for Million-Scale Generalization</h3>
    <p><span class="venue-badge">KDD 2026</span></p>
    <p class="badge-row">
      <a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2503.03137">&#128196; Paper</a>
      <a class="readme-badge code-badge" href="https://github.com/CIAM-Group/L2R">&#128187; Code</a>
    </p>
    <ul>
      <li>Proposed the first learning-based framework to dynamically prune the search space by adaptively prioritizing nodes based on problem-specific features and states.</li>
      <li>Developed <strong>the first</strong> neural solver for <strong>10-million-node</strong> VRP instances. Trained only on <strong>100-node</strong> instances, it generalizes to TSP10M in a zero-shot manner with a 5.05% gap.</li>
    </ul>
  </div>
</div>

<div class="highlight-paper-card">
  <div class="highlight-paper-image">
    <img src="images/papers/URS.png" alt="URS overview">
  </div>
  <div class="highlight-paper-body">
    <h3>URS: A Unified Neural Routing Solver for Cross-Problem Zero-Shot Generalization</h3>
    <p><span class="venue-badge">ICML 2026</span></p>
    <p class="badge-row">
      <a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2509.23413">&#128196; Paper</a>
      <a class="readme-badge code-badge" href="https://github.com/CIAM-Group/URS">&#128187; Code</a>
    </p>
    <ul>
      <li>Proposed a unified data representation that eliminates the need for problem enumeration by projecting diverse VRP variants into a unified feature space.</li>
      <li>Developed <strong>the first</strong> neural solver that efficiently solves <strong>over 100</strong> VRP variants with a single model without retraining or fine-tuning, while scaling to <strong>7,000-node</strong> instances.</li>
    </ul>
  </div>
</div>

<!-- **EasyCO: A Learning-Driven Platform for Combinatorial Optimization**  
In Development | Lead

- Established a standardized pipeline spanning data generation, environment setup, training, and evaluation.
- Currently supports standardized workflows for over **50** solvers and automated solving for over **150** combinatorial optimization problems. -->

<span class='anchor' id='publications'></span>

<h1>&#128221; Publications</h1>

## Arxiv Preprint

<ol class="publication-list">
<li class="publication-item" markdown="1">
<u>Canhong Yu</u>, **Changliang Zhou**, Rongsheng Chen, Zhenkun Wang<sup>&dagger;</sup>, Yu Zhou. Rethinking Constraint Awareness for Efficient State Embedding of Neural Routing Solver. *arXiv preprint arXiv:2605.10122*, 2026.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2605.10122">&#128196; Paper</a></p>
</li>

<li class="publication-item" markdown="1">
<u>Rongsheng Chen</u>, **Changliang Zhou**, Canhong Yu, Yuanyao Chen, Yu Zhou, Zhuo Chen, Zhenkun Wang<sup>&dagger;</sup>. SPACE: Unifying Symmetric and Asymmetric Routing Problems for Generalist Neural Solver. *arXiv preprint arXiv:2605.24484*, 2026.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2605.24484">&#128196; Paper</a></p>
</li>

<li class="publication-item" markdown="1">
Yunpeng Ba, Xi Lin, **Changliang Zhou**, Ruihao Zheng, Zhenkun Wang<sup>&dagger;</sup>, Xinyan Liang, Zhichao Lu, Jianyong Sun, Yuhua Qian, Qingfu Zhang. Survey on Neural Routing Solvers. *arXiv preprint arXiv:2602.21761*, 2026.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2602.21761">&#128196; Paper</a></p>
</li>
</ol>

## Accepted Conference Papers:

<ol class="publication-list">
<li class="publication-item" markdown="1">
<span class="venue-badge">ICML 2026</span> **Changliang Zhou**, Canhong Yu, Shunyu Yao, Xi Lin, Zhenkun Wang<sup>&dagger;</sup>, Yu Zhou, Qingfu Zhang. URS: A Unified Neural Routing Solver for Cross-Problem Zero-Shot Generalization. *43rd International Conference on Machine Learning* (**ICML**), 2026.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2509.23413">&#128196; Paper</a> <a class="readme-badge code-badge" href="https://github.com/CIAM-Group/URS">&#128187; Code</a></p>
</li>

<li class="publication-item" markdown="1">
<span class="venue-badge">KDD 2026</span> **Changliang Zhou**\*, Xi Lin\*, Zhenkun Wang<sup>&dagger;</sup>, Qingfu Zhang. Learning to Reduce Search Space for Generalizable Neural Routing Solver. *32nd SIGKDD Conference on Knowledge Discovery and Data Mining* (**KDD**), 2026.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2503.03137">&#128196; Paper</a> <a class="readme-badge code-badge" href="https://github.com/CIAM-Group/L2R">&#128187; Code</a></p>
</li>

<li class="publication-item" markdown="1">
<span class="venue-badge">NeurIPS 2024</span> Zhi Zheng, **Changliang Zhou**, Xialiang Tong, Mingxuan Yuan, Zhenkun Wang<sup>&dagger;</sup>. UDC: A Unified Neural Divide-and-Conquer Framework for Large-Scale Combinatorial Optimization Problems. *Advances in Neural Information Processing Systems* (**NeurIPS**), 2024.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8e4c8468273ee3bafb288229c0acbc-Paper-Conference.pdf">&#128196; Paper</a> <a class="readme-badge code-badge" href="https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/UDC-Large-scale-CO-master">&#128187; Code</a></p>
</li>

<li class="publication-item" markdown="1">
<span class="venue-badge">AAAI 2024</span> Yubin Xiao, Di Wang, Boyang Li, Mingzhao Wang, Xuan Wu, **Changliang Zhou**, You Zhou<sup>&dagger;</sup>. Distilling Autoregressive Models to Obtain High-Performance Non-autoregressive Solvers for Vehicle Routing Problems with Faster Inference Speed. *Proceedings of the AAAI Conference on Artificial Intelligence* (**AAAI**), 2024.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2312.12469">&#128196; Paper</a> <a class="readme-badge code-badge" href="https://github.com/xybFight/GNARKD">&#128187; Code</a></p>
</li>
</ol>

## Accepted Journal Articles:

<ol class="publication-list">
<li class="publication-item" markdown="1">
<span class="venue-badge">T-ITS 2026</span> **Changliang Zhou**\*, Xi Lin\*, Zhenkun Wang<sup>&dagger;</sup>, Xialiang Tong, Mingxuan Yuan, Qingfu Zhang. Instance-Conditioned Adaptation for Large-Scale Generalization of Neural Routing Solver. *IEEE Transactions on Intelligent Transportation Systems* (**T-ITS**), 2026.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://arxiv.org/pdf/2405.01906">&#128196; Paper</a> <a class="readme-badge code-badge" href="https://github.com/CIAM-Group/ICAM">&#128187; Code</a></p>
</li>

<li class="publication-item" markdown="1">
<span class="venue-badge">JWPE 2025</span> Sheng Miao, Xuefei Li, Huaying Sun, Xiubo Chen, **Changliang Zhou**, Xiang Shen, Chao Liu<sup>&dagger;</sup>, Changqing Liu, Weijun Gao. Multi-output Behavioral Cloning Framework: A Knowledge-Based Predictive Control Methodology Based on Deep Learning for Wastewater Treatment Plants. *Journal of Water Process Engineering* (**JWPE**), 69:106813, 2025.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://www.sciencedirect.com/science/article/abs/pii/S2214714424020452">&#128196; Paper</a></p>
</li>

<li class="publication-item" markdown="1">
<span class="venue-badge">SCS 2021</span> Sheng Miao\*<sup>&dagger;</sup>, **Changliang Zhou**\*, Salman Ali AlQahtani, Mubarak Alrashoud, Ahmed Ghoneim, Zhihan Lv. Applying Machine Learning in Intelligent Sewage Treatment: A Case Study of Chemical Plant in Sustainable Cities. *Sustainable Cities and Society* (**SCS**), 72:103009, 2021.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://www.sciencedirect.com/science/article/abs/pii/S2210670721002936">&#128196; Paper</a></p>
</li>

<li class="publication-item" markdown="1">
<span class="venue-badge">JCR 2020</span> Chao Liu<sup>&dagger;</sup>, Haoqing Zhang, Sheng Miao, Xuefei Li, Qun Miao, **Changliang Zhou**. Assessment of Status and Vulnerability to Seawater Intrusion in Wendeng District, China. *Journal of Coastal Research* (**JCR**), 104(sp1):546-553, 2020.

<p class="badge-row"><a class="readme-badge paper-badge" href="https://bioone.org/journals/journal-of-coastal-research/volume-104/issue-sp1/JCR-SI104-095.1/Assessment-of-Status-and-Vulnerability-to-Seawater-Intrusion-in-Wendeng/10.2112/JCR-SI104-095.1.short">&#128196; Paper</a></p>
</li>
</ol>

\* Equal contribution. <sup>&dagger;</sup> Corresponding author. <u>xxxx</u> names indicate co-mentored students.

<span>(Last updated May 2026.)</span>

<span class='anchor' id='education'></span>

<h1>&#127891; Education</h1>

- *Sep. 2022 - Present*, **Southern University of Science and Technology**, Ph.D. student in Intelligent Manufacturing and Robotics, School of Automation and Intelligent Manufacturing.
- *Sep. 2019 - Jun. 2022*, **Qingdao University**, M.Sc. degree in Software Engineering, College of Computer Science and Technology.

<span class='anchor' id='service-and-honors'></span>

<h1>&#127942; Service and Honors</h1>

- **Reviewer**: ICLR 2026; NeurIPS 2026.
- **University Honor**: Outstanding Postgraduate Student, Southern University of Science and Technology, 2022-2023.

<span class='anchor' id='teaching'></span>

<h1>&#128104;&#8205;&#127979; Teaching</h1>

- **Teaching Assistant**, **SDM374 Machine Learning System Design**, Southern University of Science and Technology (Fall 2023), Sep. 2023 - Jan. 2024.
- **Teaching Assistant**, **SDM374 Machine Learning System Design**, Southern University of Science and Technology (Fall 2022), Sep. 2022 - Jan. 2023.
