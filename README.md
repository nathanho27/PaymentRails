# PaymentRails

## Visa and Mastercard: Market & Competitive Analysis

Market and competitive analysis of global payment networks, focusing on Visa and Mastercard, using public financial and market data to study scale, growth, and profitability dynamics through interactive BI dashboards.

---

## Table of Contents
- [Status](#status)
- [Overview](#overview)
- [Analytical Objectives](#analytical-objectives)
- [Market Context](#market-context)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Tools & Technologies](#tools--technologies)
- [Core Analytical Dimensions](#core-analytical-dimensions)
- [Dashboards](#dashboards)
- [Visualization Approach](#visualization-approach)
- [Project Structure](#project-structure)
- [Current Progress](#current-progress)
- [Planned Work](#planned-work)
- [Notes & Limitations](#notes--limitations)

---

## Status

**In Progress**
Core data pipeline is implemented, including Python-based market data ingestion, MySQL schema design, and SQL analytics views for daily returns and rolling volatility. A BI-ready analytics table has been generated for visualization in Excel and Tableau. Dashboard development is currently underway.

---

## Overview

PaymentRails is a market analytics project that examines how large-scale payment networks compete within the global financial ecosystem. Rather than focusing on consumer-facing payment products, the project frames Visa and Mastercard as financial infrastructure providers, emphasizing transaction scale, revenue efficiency, and margin durability.

Using publicly available market and financial data, the project compares how these networks differ across market performance, growth characteristics, and profitability.

---

## Analytical Objectives

- Compare the long-term market performance of Visa and Mastercard  
- Analyze differences in scale, revenue growth, and profitability  
- Examine tradeoffs between growth, stability, and margin durability  
- Identify structural similarities and differences between payment network models  
- Replicate a realistic market analysis workflow using public data  

---

## Market Context

Payment networks operate as transaction infrastructure connecting issuing banks, merchants, and consumers. These networks benefit from strong network effects, asset-light operating models, and global scale.

Visa and Mastercard represent two of the largest and most established players in this space, making them a natural comparison set for studying how scale, efficiency, and growth interact in mature fintech markets.

---

## Data Sources

- Historical stock price data from Yahoo Finance  
- Financial statement data from public company filings  
- Aggregated financial datasets summarizing revenue and margins  
- Annual reports and investor materials for the business context  

---

## Methodology

- Pull raw market and financial data using Python  
- Clean and normalize datasets using SQL and Excel  
- Compute derived metrics (daily returns, rolling volatility) using SQL analytics views, with Python used for ingestion and export of BI-ready datasets.
- Export analysis-ready tables for Tableau Public  

---

## Tools & Technologies

- Python
- MySQL
- SQL
- pandas
- Excel / Power Query
- Tableau Public
- Git & GitHub

---

## Core Analytical Dimensions

### Market Performance
- Indexed stock price trends  
- Relative returns and volatility  

### Scale & Transaction Activity
- Reported payment volume as a proxy for network scale  
- Growth trends in transaction activity  

### Revenue & Monetization
- Revenue growth over time  
- Monetization efficiency indicators  

### Profitability
- Gross and operating margin trends  
- Margin stability across cycles  

---

## Dashboards

1. Market Performance Overview  
2. Revenue & Growth Trends  
3. Scale & Transaction Activity  
4. Profitability & Margins  
5. Competitive Summary  

---

## Visualization Approach

Dashboards are built in Tableau Public and designed for exploratory comparison rather than operational reporting, prioritizing clarity and narrative flow.

---

## Project Structure

```
PaymentRails/
├── src/
│   ├── __init__.py
│   ├── stock_load.py
│   ├── financial_load.py
│   ├── data_transformation.py
│   ├── metrics_build.py
│   └── tableau_export.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── analytics/
│
├── sql/
│   ├── analytics/
│   │   ├── daily_returns.sql
│   │   ├── volatility.sql
│   │   └── market_metrics.sql
│   └── schema/
│       ├── raw_market_prices.sql
│       └── clean_market_prices.sql
│
├── dashboards/
├── docs/
├── excel/
└── README.md
```

---

## Current Progress
- Implemented Python ingestion for Visa, Mastercard, and market index data  
- Built MySQL analytics layer with daily returns and rolling volatility  
- Exported final analytics table for visualization in Excel and Tableau
  
## Planned Work

- Ingest and index historical stock price data  
- Compile and standardize financial metrics  
- Build Tableau Public dashboards  
- Refine insights as visuals are completed  

---

## Notes & Limitations

This project uses public financial data and focuses on descriptive, comparative analysis rather than forecasting or investment recommendations.

This project marks a shift in my Python coding style, where I moved from CamelCase to snake_case for functions, variables, and filenames to align with Python consistency.
