### Special events trading — datasets + pipelines (03)

This document focuses on **what text datasets each paper uses** (source, unit, size, timeframe) and **what the main pipeline/algorithm does**.

---

### A) Text datasets used (table)

| Paper | Text dataset(s) | Unit | Universe | Timeframe | Size (stated) | Target / label |
|---|---|---|---|---|---|---|
| **Legal risk (LLM signal)** (`Oral-Legal-Risk.pdf`) | SEC EDGAR 10‑Q/10‑K (Legal Proceedings + footnotes)<br>Ancillary: Yahoo Finance; Zacks | Filing section pair | 1,200 NASDAQ/NYSE → 734 “high-quality” | **Feb 2020 → May 2025** | **734 firms** | LLM legal-risk change score → monthly long–short |
| **TRR crash detection** (`lm-detect-crash.pdf`) | Reuters financial news dataset (unfiltered)<br>Ancillary: Yahoo Finance prices | Day (news set) | Two portfolios: country‑neutral + sector‑neutral | 2007 / 2010 / 2020 crisis windows<br>+ 2012 stable<br>+ 2021–2022 post‑cutoff | (Varies by window) | Next‑day crash label (portfolio return ≤ −2.0%) |
| **FinRipple (event ripple)** (`Oral-FinRipple.pdf`) | News about S&P 500 companies<br>+ time‑varying financial KG | News item (+ KG ctx) | S&P 500 | Test: **2020‑01‑01 → 2022‑06‑30**<br>Backtest: **2020‑01 → 2022‑06** | **10,000 test**<br>~110,000 train | Impact prediction; explains CAPM residuals; long–short portfolio |
| **RiskLabs (position paper)** (`Oral-RiskLabs.pdf`) | ECC transcripts + daily news (plus audio + time series) | (Not specified) | (Not specified) | (Not specified) | (Not specified) | Volatility (3/7/15/30‑day) + 95% VaR |

**Notes (dataset details / filters)**
- **Oral-Legal-Risk**: text is explicitly *extracted sections* (Legal Proceedings item + relevant footnotes); “high‑quality” defined as ≥200 characters.
- **lm-detect-crash**: uses Reuters financial news dataset and extends it to 2020; evaluates over multiple explicitly named windows; deep baselines use a larger Reuters training split, but TRR is evaluated as a zero-shot reasoning framework.
- **RiskLabs**: main body describes modalities and an experimental setup, but does not clearly specify a single dataset source/timeframe in the extracted main text (so we mark as “not specified” here rather than guessing).

---

### B) Main algorithm / pipeline (table)

| Paper | Pipeline (high level) | Output(s) |
|---|---|---|
| **Oral-Legal-Risk** | Pull filings → extract Legal Proceedings sections → filter/clean → GPT‑4o scores change between adjacent filings → build monthly long–short portfolios (tanh weighting with vol + score) → evaluate vs factors/mirror | Legal‑risk change score; portfolio returns + alpha |
| **lm-detect-crash (TRR)** | For each day: LLM generates impact chains (news → entities → portfolio stocks) → store/retrieve decayed memory → PageRank attention to filter chains → LLM reasons over temporal tuples to predict next‑day crash | Next‑day crash prediction; AUROC across windows/portfolios |
| **FinRipple** | Build time‑varying financial KG → inject KG via adapters → PPO fine‑tune LLM backbone for market alignment → infer ripple impacts using news + KG context → evaluate via CAPM residual explanation + portfolio backtests | Impact predictions; explanatory power; portfolio performance |
| **RiskLabs** | Encode ECC audio/text + LLM analysis features + news features + time‑series → fuse → multi‑task heads for volatility horizons and VaR | Volatility + VaR forecasts; comparative results |


