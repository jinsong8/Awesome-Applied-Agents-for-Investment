# Awesome Applied Agents for Investment

A curated, structured collection of papers and artifacts on LLMs, agentic systems, and
applied AI for investment research, trading, risk, and financial text analysis. The goal
is to make it easy to browse the landscape, compare approaches, and build reading packs
for focused study or replication.

## Repository Organization

- `00_Surveys/`: broad overviews of LLMs and AI in quantitative investing.
- `01_Agentic_Trading_and_Strategy_Automation/`: agent-based trading systems, strategy
  automation, multi-agent markets, and forecasting agents.
- `02_Text_Signals_from_News_Calls_Filings/`: text-derived signals from news, calls,
  filings, and corporate communication.
- `03_Risk_Crash_and_Volatility/`: risk prediction, crash detection, and volatility
  modeling with LLMs.
- `04_IE_and_Interpretable_Text_Methods/`: information extraction and interpretable NLP
  methods tailored to finance.
- `05_Benchmarks_and_Datasets/`: benchmarks, datasets, and evaluation suites.
- `reading_packets/`: Markdown reading packets per paper (notes, snippets, or outlines).
- `extracted/`: extracted plain text from PDFs.
- `deep_extracted/`: deeper extraction outputs for longer-form text capture.
- `tools/`: scripts for extraction and section scanning.
- `section_index.json`: lookup table for section hits across extracted texts.

## Paper Highlights (one line each)

### 00 Surveys
- [AI4QuantInvest-Survey](00_Surveys/AI4QuantInvest-Survey.pdf) ([source](https://arxiv.org/abs/2503.21422)): survey of AI methods in quantitative investment research. Title: From Deep Learning to LLMs: A survey of AI in Quantitative Investment.
- [Equity-Markets-LLM-Survey](00_Surveys/Equity-Markets-LLM-Survey.pdf) ([source](https://doi.org/10.3389/frai.2025.1608365)): LLM use cases and results in equity markets. Title: Large Language Models in equity markets: applications, techniques, and insights.
- [The-New-Quant-Survey](00_Surveys/The-New-Quant-Survey.pdf) ([source](https://arxiv.org/abs/2510.05533)): overview of modern quant workflows and model trends. Title: The New Quant: A Survey of Large Language Models in Financial Prediction and Trading.

### 01 Agentic Trading and Strategy Automation
- [AAPM-LLM-Agent-Asset-Pricing](01_Agentic_Trading_and_Strategy_Automation/AAPM-LLM-Agent-Asset-Pricing.pdf) ([source](https://arxiv.org/abs/2409.17266)): LLM agent for asset pricing and market reasoning. Title: Empirical Asset Pricing with Large Language Model Agents.
- [AIA-Forecaster](01_Agentic_Trading_and_Strategy_Automation/AIA-Forecaster.pdf) ([source](https://arxiv.org/abs/2511.07678)): agentic forecasting framework for market prediction. Title: AIA Forecaster: Technical Report.
- [Alpha-GPT](01_Agentic_Trading_and_Strategy_Automation/Alpha-GPT.pdf) ([source](https://arxiv.org/abs/2308.00016)): GPT-style approach to alpha generation. Title: Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment.
- [Alpha-Jungle-MCTS](01_Agentic_Trading_and_Strategy_Automation/Alpha-Jungle-MCTS.pdf) ([source](https://arxiv.org/abs/2505.11122)): MCTS-driven search for trading strategies. Title: Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining.
- [Alpha-R1](01_Agentic_Trading_and_Strategy_Automation/Alpha-R1.pdf) ([source](https://arxiv.org/abs/2512.23515)): RL-style agent for trading or market decision tasks. Title: Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning.
- [AlphaAgent](01_Agentic_Trading_and_Strategy_Automation/AlphaAgent.pdf) ([source](https://arxiv.org/abs/2502.16789)): agent-based trading decision architecture. Title: AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay.
- [AlphaForge](01_Agentic_Trading_and_Strategy_Automation/AlphaForge.pdf) ([source](https://arxiv.org/abs/2406.18394)): automated alpha factor discovery pipeline. Title: AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors.
- [AlphaQuanter](01_Agentic_Trading_and_Strategy_Automation/AlphaQuanter.pdf) ([source](https://arxiv.org/abs/2510.14264)): LLM-enhanced quant research workflow. Title: AlphaQuanter: An End-to-End Tool-Orchestrated Agentic Reinforcement Learning Framework for Stock Trading.
- [Approaching-Human-Level-Forecasting](01_Agentic_Trading_and_Strategy_Automation/Approaching-Human-Level-Forecasting.pdf) ([source](https://arxiv.org/abs/2402.18563)): improved forecasting performance with LLMs. Title: Approaching Human-Level Forecasting with Language Models.
- [Can-LLMs-Trade-Market-Sim](01_Agentic_Trading_and_Strategy_Automation/Can-LLMs-Trade-Market-Sim.pdf) ([source](https://arxiv.org/abs/2504.10789)): LLM trading in market simulation environments. Title: Can Large Language Models Trade? Testing Financial Theories with LLM Agents in Market Simulations.
- [ChatGPT-Abnormal-Returns](01_Agentic_Trading_and_Strategy_Automation/ChatGPT-Abnormal-Returns.pdf) ([source](https://doi.org/10.61351/mf.v3i3.327)): using ChatGPT-style signals for return prediction. Title: Could ChatGPT have earned abnormal returns? A retrospective test from the U.S. stock market.
- [ChatGPT-Portfolio-Selection](01_Agentic_Trading_and_Strategy_Automation/ChatGPT-Portfolio-Selection.pdf) ([source](https://arxiv.org/abs/2308.06260)): LLM assistance for portfolio construction. Title: ChatGPT-based Investment Portfolio Selection.
- [Cognitive-Alpha-Mining](01_Agentic_Trading_and_Strategy_Automation/Cognitive-Alpha-Mining.pdf) ([source](https://arxiv.org/abs/2511.18850)): cognitive-style alpha mining with LLMs. Title: Cognitive Alpha Mining via LLM-Driven Code-Based Evolution.
- [FINMEM](01_Agentic_Trading_and_Strategy_Automation/FINMEM.pdf) ([source](https://arxiv.org/abs/2311.13743)): memory-augmented LLMs for financial reasoning tasks. Title: FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design.
- [FLAG-TRADER](01_Agentic_Trading_and_Strategy_Automation/FLAG-TRADER.pdf) ([source](https://arxiv.org/abs/2502.11433)): LLM trading agent with feedback or guardrails. Title: FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading.
- [FinCon](01_Agentic_Trading_and_Strategy_Automation/FinCon.pdf) ([source](https://arxiv.org/abs/2407.06567)): LLM-based financial conversation or decision agent. Title: FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making.
- [FinRpt-Equity-Research-Report-Generation](01_Agentic_Trading_and_Strategy_Automation/FinRpt-Equity-Research-Report-Generation.pdf) ([source](https://arxiv.org/abs/2511.07322)): first comprehensive framework for automating Equity Research Report generation using LLMs, featuring a dataset integrating 7 financial data types, an 11-metric evaluation system, and a multi-agent framework with SFT and RL training. Title: FinRpt: Dataset, Evaluation System and LLM-based Multi-agent Framework for Equity Research Report Generation.
- [FinVision-Multi-Agent-Prediction](01_Agentic_Trading_and_Strategy_Automation/FinVision-Multi-Agent-Prediction.pdf) ([source](https://arxiv.org/abs/2411.08899)): multi-agent prediction system for markets. Title: FinVision: A Multi-Agent Framework for Stock Market Prediction.
- [GPT-Stock-Factors](01_Agentic_Trading_and_Strategy_Automation/GPT-Stock-Factors.pdf) ([source](https://ssrn.com/abstract=4560216)): LLMs for stock factor generation. Title: GPT's Idea of Stock Factors.
- [LLM-Crypto-Portfolio-Management](01_Agentic_Trading_and_Strategy_Automation/LLM-Crypto-Portfolio-Management.pdf) ([source](https://arxiv.org/abs/2501.00826)): LLM-guided crypto portfolio management. Title: LLM-Powered Multi-Agent System for Automated Crypto Portfolio Management.
- [MarketSenseAI-2](01_Agentic_Trading_and_Strategy_Automation/MarketSenseAI-2.pdf) ([source](https://arxiv.org/abs/2502.00415)): market-sensing agent for trading signals. Title: MarketSenseAI 2.0: Enhancing Stock Analysis through LLM Agents.
- [MountainLion-Multimodal-Trading](01_Agentic_Trading_and_Strategy_Automation/MountainLion-Multimodal-Trading.pdf) ([source](https://arxiv.org/abs/2507.20474)): multimodal inputs for trading agents. Title: MountainLion: A Multi-Modal LLM-Based Agent System for Interpretable and Adaptive Financial Trading.
- [Multimodal-Foundation-Agent](01_Agentic_Trading_and_Strategy_Automation/Multimodal-Foundation-Agent.pdf) ([source](https://arxiv.org/abs/2402.18485)): foundation agent with multimodal financial inputs. Title: A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist.
- [P1GPT-Multimodal-Finance-Analysis](01_Agentic_Trading_and_Strategy_Automation/P1GPT-Multimodal-Finance-Analysis.pdf) ([source](https://arxiv.org/abs/2510.23032)): multimodal LLM for finance analysis. Title: P1GPT: a multi-agent LLM workflow module for multi-modal financial information analysis.
- [QuantEvolve](01_Agentic_Trading_and_Strategy_Automation/QuantEvolve.pdf) ([source](https://arxiv.org/abs/2510.18569)): evolutionary or adaptive quant research agent. Title: QuantEvolve: Automating Quantitative Strategy Discovery through Multi-Agent Evolutionary Framework.
- [RD-Agent-Quant](01_Agentic_Trading_and_Strategy_Automation/RD-Agent-Quant.pdf) ([source](https://arxiv.org/abs/2505.15155)): R&D style agent for quant research. Title: R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization.
- [StockAgent-Simulated-Trading](01_Agentic_Trading_and_Strategy_Automation/StockAgent-Simulated-Trading.pdf) ([source](https://arxiv.org/abs/2407.18957)): simulated trading with agent-based systems. Title: When AI Meets Finance (StockAgent): Large Language Model-based Stock Trading in Simulated Real-world Environments.
- [TraderTalk-LLM-ABM-Trading](01_Agentic_Trading_and_Strategy_Automation/TraderTalk-LLM-ABM-Trading.pdf) ([source](https://arxiv.org/abs/2410.21280)): agent-based market with LLM trader agents. Title: TraderTalk: An LLM Behavioural ABM applied to Simulating Human Bilateral Trading Interactions.
- [TradingAgents](01_Agentic_Trading_and_Strategy_Automation/TradingAgents.pdf) ([source](https://arxiv.org/abs/2412.20138)): multi-agent setups for trading workflows. Title: TradingAgents: Multi-Agents LLM Financial Trading Framework.
- [What-Drives-Performance](01_Agentic_Trading_and_Strategy_Automation/What-Drives-Performance.pdf) ([source](https://doi.org/10.2139/ssrn.5851562)): analysis of performance drivers in agentic trading. Title: What Drives the Performance of Machine Learning Factor Strategies?.

### 02 Text Signals from News, Calls, and Filings
- [ChatGPT-Corporate-Policy-Investment-Score](02_Text_Signals_from_News_Calls_Filings/ChatGPT-Corporate-Policy-Investment-Score.pdf) ([source](http://www.nber.org/papers/w32161)): policy language mapped to investable scores. Title: ChatGPT and Corporate Policies.
- [ECC-Analyzer-LLM-Volatility](02_Text_Signals_from_News_Calls_Filings/ECC-Analyzer-LLM-Volatility.pdf) ([source](https://arxiv.org/abs/2404.18470)): earnings call analysis for volatility signals. Title: ECC Analyzer: Extract Trading Signal from Earnings Conference Calls using Large Language Model for Stock Performance Prediction.
- [FinLlama](02_Text_Signals_from_News_Calls_Filings/FinLlama.pdf) ([source](https://arxiv.org/abs/2403.12285)): finance-tuned LLM for textual signal extraction. Title: FinLlama: Financial Sentiment Classification for Algorithmic Trading Applications.
- [Financial-News-Structured-Extraction](02_Text_Signals_from_News_Calls_Filings/Financial-News-Structured-Extraction.pdf) ([source](https://arxiv.org/abs/2407.15788)): structured extraction from financial news. Title: Extracting Structured Insights from Financial News: An Augmented LLM Driven Approach.
- [LLM-Core-Earnings](02_Text_Signals_from_News_Calls_Filings/LLM-Core-Earnings.pdf) ([source](https://doi.org/10.2139/ssrn.4979501)): LLM-driven extraction of core earnings signals. Title: Scaling Core Earnings Measurement with Large Language Models.
- [LLM-Market-Sentiment](02_Text_Signals_from_News_Calls_Filings/LLM-Market-Sentiment.pdf) ([source](https://doi.org/10.2139/ssrn.4584928)): market sentiment from financial text. Title: Large Language Models and Financial Market Sentiment.
- [LLM-Sentiment-Trading](02_Text_Signals_from_News_Calls_Filings/LLM-Sentiment-Trading.pdf) ([source](https://doi.org/10.1016/j.frl.2024.105227)): sentiment-driven trading via LLMs. Title: Sentiment trading with large language models.

### 03 Risk, Crash, and Volatility
- [FinRipple-Event-Ripple-Effects](03_Risk_Crash_and_Volatility/FinRipple-Event-Ripple-Effects.pdf) ([source](https://arxiv.org/abs/2505.23826)): event ripple effects and systemic risk. Title: FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness.
- [LLM-Legal-Risk-Signal](03_Risk_Crash_and_Volatility/LLM-Legal-Risk-Signal.pdf) ([source](https://doi.org/10.64336/001c.144303)): legal risk inference from text. Title: Quantifying legal risk with Large Language Models: A text-based investment signal.
- [LLM-Portfolio-Crash-Detection](03_Risk_Crash_and_Volatility/LLM-Portfolio-Crash-Detection.pdf) ([source](https://arxiv.org/abs/2410.17266)): LLM-based crash detection signals. Title: Temporal Relational Reasoning of Large Language Models for Detecting Stock Portfolio Crashes.
- [RiskLabs-LLM-Risk-Prediction](03_Risk_Crash_and_Volatility/RiskLabs-LLM-Risk-Prediction.pdf) ([source](https://arxiv.org/abs/2404.07452)): risk prediction with LLMs. Title: RiskLabs: Predicting Financial Risk Using Large Language Model based on Multimodal and Multi-Sources Data.

### 04 IE and Interpretable Text Methods
- [ADELIE-IE-Alignment](04_IE_and_Interpretable_Text_Methods/ADELIE-IE-Alignment.pdf) ([source](https://arxiv.org/abs/2405.05008)): alignment-focused information extraction. Title: ADELIE: Aligning Large Language Models on Information Extraction.
- [LDA-Robustness-Text-Analysis](04_IE_and_Interpretable_Text_Methods/LDA-Robustness-Text-Analysis.pdf) ([source](https://doi.org/10.3982/qe1825)): topic model robustness in finance. Title: Robust machine learning algorithms for text analysis.
- [LLM-Interpretable-Feature-Generation](04_IE_and_Interpretable_Text_Methods/LLM-Interpretable-Feature-Generation.pdf) ([source](https://arxiv.org/abs/2409.07132)): interpretable features generated by LLMs. Title: LLM-based feature generation from text for interpretable machine learning.

### 05 Benchmarks and Datasets
- [CFA-LLM-Benchmark](05_Benchmarks_and_Datasets/CFA-LLM-Benchmark.pdf) ([source](https://arxiv.org/abs/2509.04468)): CFA-style evaluation benchmark. Title: Evaluating Large Language Models for Financial Reasoning: A CFA-Based Benchmark Study.
- [FinGPT](05_Benchmarks_and_Datasets/FinGPT.pdf) ([source](https://arxiv.org/abs/2306.06031)): domain-specific financial LLM benchmark/model. Title: FinGPT: Open-Source Financial Large Language Models.
- [FinTagging](05_Benchmarks_and_Datasets/FinTagging.pdf) ([source](https://arxiv.org/abs/2505.20650)): financial tagging benchmark or dataset. Title: FinTagging: Benchmarking LLMs for Extracting and Structuring Financial Information.
- [LiveTradeBench](05_Benchmarks_and_Datasets/LiveTradeBench.pdf) ([source](https://arxiv.org/abs/2511.03628)): trading benchmark for live-style evaluation. Title: LiveTradeBench: Seeking Real-World Alpha with Large Language Models.
- [MultiFinBen](05_Benchmarks_and_Datasets/MultiFinBen.pdf) ([source](https://arxiv.org/abs/2506.14028)): multi-task finance benchmark. Title: MultiFinBen: Benchmarking Large Language Models for Multilingual and Multimodal Financial Application.
- [Profit-Mirage-LLM-Agent-Leakage](05_Benchmarks_and_Datasets/Profit-Mirage-LLM-Agent-Leakage.pdf) ([source](https://arxiv.org/abs/2510.07920)): evaluation leakage analysis. Title: Profit Mirage: Revisiting Information Leakage in LLM-based Financial Agents.

## Tools

The `tools/` folder includes scripts for:
- extracting text from PDFs,
- scanning sections across papers,
- generating reading packets.

If you add new PDFs, place them in the appropriate category and (optionally) rerun the
tooling to update extracted artifacts and reading packets.
