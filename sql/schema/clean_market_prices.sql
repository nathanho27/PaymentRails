-- clean_market_prices.sql
-- Defines cleaned market price table used for downstream analytics
-- Creates a cleaned view of raw market price data for downstream analytics.
-- This layer enforces basic data quality constraints and standardizes the raw
-- ingestion table into an analysis-ready format.

DROP VIEW IF EXISTS clean_market_prices;

CREATE VIEW clean_market_prices AS
SELECT
  date,
  UPPER(ticker) AS ticker,
  adj_close
FROM raw_market_prices
WHERE
  date IS NOT NULL
  AND ticker IS NOT NULL
  AND adj_close IS NOT NULL
ORDER BY ticker, date;