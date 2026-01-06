### Text-derived investment signals — datasets + pipelines (02)

This document focuses on **what text datasets each paper uses** (source, unit, size, timeframe) and **what the main pipeline/algorithm does**.

---

### A) Text datasets used (table)

| Paper | Text dataset(s) | Unit | Universe | Timeframe | Size (stated) | Target / label |
|---|---|---|---|---|---|---|
| **Sentiment trading with LLMs** (`Oral-Sentiment-Trading.pdf`) | Refinitiv news<br>+ CRSP returns | Article | US stocks (AMEX/NASDAQ/NYSE) | **2010‑01‑01 → 2023‑06‑30** | **965,375 articles** | Returns / long–short trading from sentiment |
| **LLMs and Financial Market Sentiment** (`OralLLM-Sentiment.pdf`) | Reuters end‑of‑day market summaries (web‑scraped)<br>+ market/controls | Day | S&P 500 aggregate market | **2000‑01‑01 → 2020‑07‑31** | **5,142 days** | Next‑day (and weekly/monthly) S&P 500 return forecasting + CER |
| **ChatGPT and Corporate Policies** (`Oral-Investment-Score-Corperate-Policies.pdf`) | Earnings call transcripts (Seeking Alpha)<br>+ Compustat/CRSP + Duke CFO survey | Firm‑quarter | US public firms | **2006 → 2020** | **74,586 firm‑quarters** | Predict future investment + returns; validate vs CFO survey |
| **Polygon.io news IE (augmented LLM)** (`Oral-Polygon-Extraction.pdf`) | News articles (pipeline input)<br>Eval: 2023 sample across 6 providers | Article | US common stock + ADR (eval) | **2023 (eval)** | **5,530 articles** | Extract “relevant tickers” + ticker‑level sentiment |
| **Scaling Core Earnings with LLMs** (`Oral-Shaffer.pdf`) | SEC EDGAR 10‑Ks<br>linked to Compustat‑CRSP (CCM) | CIK‑year | US public firms (filtered CCM) | **FY 2000 → 2023** | **35,060 10‑Ks** (retrieved) | Core‑earnings estimates (LLM) |
| **ECC Analyzer** (`Oral-Cao.pdf`) | S&P 500 ECC dataset (audio + transcripts)<br>Labels: Yahoo Finance prices | Call | S&P 500 firms | **2017 calls** | **572 calls** | Volatility prediction (3/7/15/30‑day) |

**Notes (dataset details / filters)**
- **Oral-Sentiment-Trading**: Refinitiv “all news” matched = 2,732,845 → single‑stock = 1,865,372 → unique (dedup by cosine similarity) = 965,375.
- **OralLLM-Sentiment**: Table reports 9,582,924 characters / 1,361,444 words across the 5,142 daily summaries; controls include S&P 500 returns (Refinitiv Datastream/Eikon) and macro/credit series (FRED/Welch‑Goyal).
- **Oral-Investment-Score-Corperate-Policies**: raw transcripts 160,195 → merged 115,620 → final 74,586 firm‑quarters across 3,878 firms.
- **Oral-Shaffer**: starts from CCM 2000–2023 panel; scrapes EDGAR and extracts clean text before LLM calls (paper also mentions “~2000–2024” at a high level).

---

### B) Main algorithm / pipeline (table)

| Paper | Pipeline (high level) | Output(s) |
|---|---|---|
| **Oral-Sentiment-Trading** | Filter + dedup articles → score sentiment (OPT/BERT/FinBERT/LM dict) → predict returns + form sentiment‑sorted long–short portfolios (with costs) | Sentiment scores; predictability; strategy performance |
| **OralLLM-Sentiment** | Prompt ChatGPT (temp=0) on each daily summary → parse numeric sentiment → regress returns (daily/weekly/monthly) + out‑of‑sample portfolio allocation (CER/Sharpe) | Daily sentiment index; forecasting + allocation metrics |
| **Oral-Investment-Score-Corperate-Policies** | Chunk transcript (~2,500 words) → ask 5‑choice capex question → map to score (−1…+1) → average to firm‑quarter score → validate + predict future investment/returns | Firm‑quarter “ChatGPT Investment Score” + empirical results |
| **Oral-Polygon-Extraction** | LLM extracts tickers + ticker‑level sentiment + summary → validate ticker mapping (CIK/ticker db + string match) → enrich/store/serve → eval vs provider tickers | Structured article records + evaluation results |
| **Oral-Shaffer** | Build CCM panel → scrape EDGAR 10‑Ks → clean text → run two prompting strategies (one‑shot “Lazy Analyst” vs multi‑step “Sequential Prompt”) → validate vs benchmarks | LLM core‑earnings measures + validation tests |
| **Oral-Cao (ECC Analyzer)** | Audio+text encoders → LLM paragraph summaries → RAG retrieves “focus sentences” using question bank → fuse raw + summary + focus features → train volatility regressor (MSE) | Volatility forecasts (3/7/15/30‑day) |


