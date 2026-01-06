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
- `AI4QuantInvest-Survey.pdf`: survey of AI methods in quantitative investment research.
- `Equity-Markets-LLM-Survey.pdf`: LLM use cases and results in equity markets.
- `The-New-Quant-Survey.pdf`: overview of modern quant workflows and model trends.

### 01 Agentic Trading and Strategy Automation
- `AAPM-LLM-Agent-Asset-Pricing.pdf`: LLM agent for asset pricing and market reasoning.
- `AIA-Forecaster.pdf`: agentic forecasting framework for market prediction.
- `Alpha-GPT.pdf`: GPT-style approach to alpha generation.
- `Alpha-Jungle-MCTS.pdf`: MCTS-driven search for trading strategies.
- `Alpha-R1.pdf`: RL-style agent for trading or market decision tasks.
- `AlphaAgent.pdf`: agent-based trading decision architecture.
- `AlphaForge.pdf`: automated alpha factor discovery pipeline.
- `AlphaQuanter.pdf`: LLM-enhanced quant research workflow.
- `Approaching-Human-Level-Forecasting.pdf`: improved forecasting performance with LLMs.
- `Can-LLMs-Trade-Market-Sim.pdf`: LLM trading in market simulation environments.
- `ChatGPT-Abnormal-Returns.pdf`: using ChatGPT-style signals for return prediction.
- `ChatGPT-Portfolio-Selection.pdf`: LLM assistance for portfolio construction.
- `Cognitive-Alpha-Mining.pdf`: cognitive-style alpha mining with LLMs.
- `Evolutionary-Alpha-Factor-Discovery.pdf`: evolutionary search for alpha factors.
- `FINMEM.pdf`: memory-augmented LLMs for financial reasoning tasks.
- `FLAG-TRADER.pdf`: LLM trading agent with feedback or guardrails.
- `FinCon.pdf`: LLM-based financial conversation or decision agent.
- `FinVision-Multi-Agent-Prediction.pdf`: multi-agent prediction system for markets.
- `GPT-Stock-Factors.pdf`: LLMs for stock factor generation.
- `LLM-Crypto-Portfolio-Management.pdf`: LLM-guided crypto portfolio management.
- `MarketSenseAI-2.pdf`: market-sensing agent for trading signals.
- `MountainLion-Multimodal-Trading.pdf`: multimodal inputs for trading agents.
- `Multimodal-Foundation-Agent.pdf`: foundation agent with multimodal financial inputs.
- `P1GPT-Multimodal-Finance-Analysis.pdf`: multimodal LLM for finance analysis.
- `QuantEvolve.pdf`: evolutionary or adaptive quant research agent.
- `RD-Agent-Quant.pdf`: R&D style agent for quant research.
- `StockAgent-Simulated-Trading.pdf`: simulated trading with agent-based systems.
- `TraderTalk-LLM-ABM-Trading.pdf`: agent-based market with LLM trader agents.
- `TradingAgents.pdf`: multi-agent setups for trading workflows.
- `What-Drives-Performance.pdf`: analysis of performance drivers in agentic trading.

### 02 Text Signals from News, Calls, and Filings
- `ChatGPT-Corporate-Policy-Investment-Score.pdf`: policy language mapped to investable scores.
- `ECC-Analyzer-LLM-Volatility.pdf`: earnings call analysis for volatility signals.
- `FinLlama.pdf`: finance-tuned LLM for textual signal extraction.
- `Financial-News-Structured-Extraction.pdf`: structured extraction from financial news.
- `LLM-Core-Earnings.pdf`: LLM-driven extraction of core earnings signals.
- `LLM-Market-Sentiment.pdf`: market sentiment from financial text.
- `LLM-Sentiment-Trading.pdf`: sentiment-driven trading via LLMs.

### 03 Risk, Crash, and Volatility
- `FinRipple-Event-Ripple-Effects.pdf`: event ripple effects and systemic risk.
- `LLM-Legal-Risk-Signal.pdf`: legal risk inference from text.
- `LLM-Portfolio-Crash-Detection.pdf`: LLM-based crash detection signals.
- `RiskLabs-LLM-Risk-Prediction.pdf`: risk prediction with LLMs.

### 04 IE and Interpretable Text Methods
- `ADELIE-IE-Alignment.pdf`: alignment-focused information extraction.
- `LDA-Robustness-Text-Analysis.pdf`: topic model robustness in finance.
- `LLM-Interpretable-Feature-Generation.pdf`: interpretable features generated by LLMs.

### 05 Benchmarks and Datasets
- `CFA-LLM-Benchmark.pdf`: CFA-style evaluation benchmark.
- `FinGPT.pdf`: domain-specific financial LLM benchmark/model.
- `FinTagging.pdf`: financial tagging benchmark or dataset.
- `LiveTradeBench.pdf`: trading benchmark for live-style evaluation.
- `MultiFinBen.pdf`: multi-task finance benchmark.
- `Profit-Mirage-LLM-Agent-Leakage.pdf`: evaluation leakage analysis.

## Tools

The `tools/` folder includes scripts for:
- extracting text from PDFs,
- scanning sections across papers,
- generating reading packets.

If you add new PDFs, place them in the appropriate category and (optionally) rerun the
tooling to update extracted artifacts and reading packets.
