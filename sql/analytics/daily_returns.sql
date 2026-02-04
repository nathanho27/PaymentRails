-- daily_returns.sql
-- Computes daily returns for Visa and Mastercard from cleaned price data
-- Builds a derived analytics view that computes daily returns for each payment network ticker
-- from cleaned adjusted close price data. This serves as the base metric for downstream volatility
-- and performance analysis.

DROP VIEW IF EXISTS daily_returns;

CREATE VIEW daily_returns AS
SELECT
  date,
  ticker,
  adj_close,
  (adj_close / LAG(adj_close) OVER (PARTITION BY ticker ORDER BY date) - 1) AS daily_return
FROM clean_market_prices
ORDER BY ticker, date;

