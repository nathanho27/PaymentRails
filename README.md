# PaymentRails

## Visa and Mastercard: Market & Competitive Analysis

Market and competitive analysis of global payment networks, focusing on Visa and Mastercard. Using public financial and market data, this project explores differences in market performance, scale, growth, and profitability through an end-to-end analytics workflow and interactive BI dashboards.

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
- [How to Run](#how-to-run)
- [Key Insights](#key-insights)
- [Notes & Limitations](#notes--limitations)

---

## Status

**In Progress**

The core data pipeline, analytics layer, and primary visualization dashboards have been implemented.

Python scripts ingest market and financial data, a MySQL analytics layer computes derived metrics such as daily returns and volatility, and analysis-ready datasets are exported for use in Tableau and Excel. Interactive dashboards visualize market performance, risk-return dynamics, and financial fundamentals for Visa and Mastercard.

Additional analytical dashboards exploring market correlation and geographic revenue exposure are being developed to extend the comparative analysis.

---

## Overview

PaymentRails is a financial market analytics project that examines how global payment networks compete within the broader financial ecosystem. Rather than focusing on consumer-facing payment products, the project frames Visa and Mastercard as financial infrastructure providers that operate large-scale transaction networks.

Using publicly available financial and market data, the project analyzes differences in market performance, risk characteristics, financial fundamentals, and global revenue exposure between the two payment networks. The analysis is delivered through an end-to-end analytics pipeline combining Python data ingestion, SQL-based analytics processing, and interactive Tableau dashboards.

---

## Analytical Objectives

- Compare the long-term market performance of Visa and Mastercard relative to the broader market  
- Evaluate risk-return dynamics using metrics such as volatility and drawdowns  
- Analyze revenue growth and profitability trends across both payment networks  
- Examine structural similarities between asset-light payment infrastructure businesses  
- Build an end-to-end financial analytics workflow integrating Python, SQL, Excel, and Tableau

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

- Pull raw market and financial data using Python.
- Clean and normalize datasets using SQL transformations.
- Compute derived metrics such as daily returns and rolling volatility using SQL window functions. Python is used for ingestion and exporting BI-ready datasets.
- Export analysis-ready tables for Tableau Public. 

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

### Risk & Return
- Volatility comparisons across payment networks and the broader market  
- Drawdown analysis highlighting peak-to-trough declines  

### Financial Fundamentals
- Revenue growth over time  
- Operating margin and profitability trends  

### Market Correlation
- Relationship between payment network returns and the broader market  
- Comparative sensitivity of Visa and Mastercard to market movements  

### Global Revenue Exposure
- Geographic revenue distribution across major regions  
- Comparative international diversification between payment networks

---

## Dashboards

### 1. Payment Network Market Analysis
• The published Tableau dashboard can be found [here](https://public.tableau.com/app/profile/nathan.ho2158/viz/PaymentNetworkMarketAnalysis/PaymentNetworkAnalysis)

![Payment Network Market Analysis](dashboards/PaymentNetworkAnalysis.png)

This dashboard provides a high-level comparison of Visa and Mastercard across market performance and financial metrics. The goal is to highlight differences in growth, scale, and long-term market behavior between the two payment networks.

---

### 2. Risk vs Return Analysis
• The published Tableau dashboard can be found [here](http://public.tableau.com/app/profile/nathan.ho2158/viz/RiskVsReturnAnalysis/RiskvsReturnAnalysis)

![Risk vs Return Analysis](dashboards/RiskVsReturnAnalysis.png)

This dashboard focuses on risk-return characteristics of Visa and Mastercard relative to the broader market. Using derived metrics such as daily returns and volatility, it visualizes how the two companies compare in terms of performance stability and market risk.

---

### 3. Financial Performance Analysis
• The published Tableau dashboard can be found [here](https://public.tableau.com/app/profile/nathan.ho2158/viz/FinancialPerformanceAnalysis_17726872075600/FinancialPerformanceAnalysis)

![Financial Performance Analysis](dashboards/FinancialPerformanceAnalysis.png)

This dashboard explores company fundamentals including revenue growth, profitability, and margin performance. The analysis highlights how the operating economics of Visa and Mastercard differ despite their similar positions within the payment network ecosystem.

---

### 4. Market Correlation Analysis
This dashboard analyzes the relationship between payment network returns and the broader market by examining daily return correlations and comparative sensitivity to market movements.

---

### 5. Global Payment Network Footprint
This dashboard visualizes geographic revenue exposure across major regions, illustrating how Visa and Mastercard generate revenue globally and highlighting differences in international diversification.

## Visualization Approach

Dashboards are built using Tableau Public and Excel to support exploratory financial analysis. The visualizations emphasize comparative analysis across market performance, scale, and profitability while maintaining a clear analytical narrative.

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
│   ├── correlation_metrics.py
│   ├── geographic_metrics.py
│   └── tableau_export.py
│
├── data/
│   ├── raw/
│   │   └── market_prices.csv
│   └── analytics/
│       ├── market_metrics.csv
│       ├── summary_metrics.csv
│       └── financials.csv
│       ├── correlation_metrics.csv
│       └── geographic_revenue.csv
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
│   ├── PaymentNetworkAnalysis.png
│   ├── RiskVsReturnAnalysis.png
│   └── FinancialPerformanceAnalysis.png
│
├── excel/
│   └── MarketAnalytics.xlsx
│
└── README.md

```
## How to Run

### 1. Pull historical market data

Run the ingestion script to download historical stock price data for Visa, Mastercard, and the S&P 500.

```bash
python src/stock_load.py
```

This script saves the raw dataset to:

```
data/raw/market_prices.csv
```

---

### 2. Load financial fundamentals

Run the financial ingestion script to build the fundamentals dataset used in the analysis.

```bash
python src/financial_load.py
```

This generates the dataset used for revenue, profitability, and margin analysis.

---

### 3. Transform and prepare datasets

Normalize and clean the datasets before loading them into the analytics layer.

```bash
python src/data_transformation.py
```

---

### 4. Build core market analytics metrics

Generate derived metrics used in the financial analysis and dashboards.

```bash
python src/metrics_build.py
```

This step computes key analytics metrics including:

- Daily returns  
- Rolling volatility  
- Summary market statistics  

---

### 5. Generate extended analytics datasets

Run additional analytics scripts used for advanced dashboards.

```bash
python src/correlation_metrics.py
python src/geographic_metrics.py
```

These scripts generate datasets used for:

- Market correlation analysis between payment networks and the broader market
- Geographic revenue exposure across major global regions

---

### 6. Run SQL analytics layer

Open a MySQL session and select the project database:

```sql
USE paymentrails;
```

Execute the schema and analytics scripts:

```sql
SOURCE sql/schema/raw_market_prices.sql;
SOURCE sql/schema/clean_market_prices.sql;
SOURCE sql/analytics/daily_returns.sql;
SOURCE sql/analytics/volatility.sql;
SOURCE sql/analytics/market_metrics.sql;
```

These scripts compute the analytics tables used to compare Visa, Mastercard, and the S&P 500 across performance and risk metrics.

---

### 7. Export BI-ready datasets

Export the final analytics tables for visualization.

```bash
python src/tableau_export.py
```

This generates CSV files in:

```
data/analytics/
```

---

### 8. Open visualization and analysis tools

The exported datasets power:

- **Tableau Public dashboards** for interactive visualization  
- **Excel workbook (`excel/MarketAnalytics.xlsx`)** for additional exploratory financial analysis

---

## Key Insights

Initial analysis highlights several structural similarities between Visa and Mastercard:

- Both payment networks have significantly outperformed the broader market over long horizons, reflecting the scalability and durability of the global payments infrastructure model.
- Mastercard exhibits slightly higher volatility and deeper historical drawdowns, indicating marginally higher sensitivity to market cycles.
- Visa demonstrates a somewhat more stable risk profile while maintaining comparable long-term growth and market performance.
- Both firms benefit from asset-light operating models driven by strong global network effects, enabling high operating margins and consistent revenue growth.

Together, these findings highlight the structural advantages of global payment networks and their ability to generate durable long-term performance.

---

## Notes & Limitations

This project uses publicly available financial and market data and focuses on descriptive comparative analysis rather than forecasting or investment recommendations.

The project also reflects a transition in my Python coding style from CamelCase to snake_case for functions, variables, and filenames to better align with Python development conventions.
