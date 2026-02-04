-- market_metrics.sql
-- Builds a final analytics-ready view combining prices, daily returns,
-- and rolling volatility into a single flat dataset for BI tools.

DROP VIEW IF EXISTS market_metrics;

CREATE VIEW market_metrics AS
SELECT
  p.date,
  p.ticker,
  p.adj_close,
  r.daily_return,
  v.rolling_30d_volatility
FROM clean_market_prices p
LEFT JOIN daily_returns r
  ON p.date = r.date AND p.ticker = r.ticker
LEFT JOIN rolling_volatility v
  ON p.date = v.date AND p.ticker = v.ticker
ORDER BY p.ticker, p.date;