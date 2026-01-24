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
- [Planned Work](#planned-work)
- [Notes & Limitations](#notes--limitations)

---

## Status

**In Progress**

Project scaffolding and documentation are complete. Historical stock price data ingestion and indexing for Visa and Mastercard is planned as the first analytical step. Financial and transaction-scale metrics will be compiled from public filings and aggregated sources. Interactive dashboard development in Tableau Public will follow once core datasets are finalized.

---

## Overview

PaymentRails is a market analytics project that examines how large-scale payment networks compete within the global financial ecosystem. Rather than focusing on consumer-facing payment products, the project frames Visa and Mastercard as financial infrastructure providers, emphasizing transaction scale, revenue efficiency, and margin durability.

Using publicly available market and financial data, the project compares how these networks differ across market performance, growth characteristics, and profitability.

---

## Analytical Objectives

- Compare long-term market performance of Visa and Mastercard  
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
- Annual reports and investor materials for business context  

---

## Methodology

- Pull raw market and financial data using Python  
- Clean and normalize datasets using Excel and Power Query where appropriate  
- Compute derived metrics and comparative measures in Python  
- Export analysis-ready tables for Tableau Public  

---

## Tools & Technologies

- Python  
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
│   ├── StockLoad.py
│   ├── FinancialLoad.py
│   ├── DataTransformation.py
│   ├── MetricsBuild.py
│   └── TableauExport.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── analytics/
├── dashboards/
├── docs/
├── README.md
```

---

## Planned Work

- Ingest and index historical stock price data  
- Compile and standardize financial metrics  
- Build Tableau Public dashboards  
- Refine insights as visuals are completed  

---

## Notes & Limitations

This project uses public financial data and focuses on descriptive, comparative analysis rather than forecasting or investment recommendations.
