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

  v.rolling_30d_volatility,

  -- normalized price (start = 100)
  p.adj_close /
  FIRST_VALUE(p.adj_close) OVER (
    PARTITION BY p.ticker
    ORDER BY p.date
  ) * 100 AS normalized_price,

  -- cumulative return
  p.adj_close /
  FIRST_VALUE(p.adj_close) OVER (
    PARTITION BY p.ticker
    ORDER BY p.date
  ) - 1 AS cumulative_return,

  -- 90 day return (momentum)
  p.adj_close /
  LAG(p.adj_close, 90) OVER (
    PARTITION BY p.ticker
    ORDER BY p.date
  ) - 1 AS rolling_90d_return,

  -- drawdown (distance from peak)
  p.adj_close /
  MAX(p.adj_close) OVER (
    PARTITION BY p.ticker
    ORDER BY p.date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) - 1 AS drawdown

FROM clean_market_prices p

LEFT JOIN daily_returns r
  ON p.date = r.date AND p.ticker = r.ticker

LEFT JOIN rolling_volatility v
  ON p.date = v.date AND p.ticker = v.ticker

WHERE p.ticker IN ('V', 'MA', '^GSPC')

ORDER BY p.ticker, p.date;