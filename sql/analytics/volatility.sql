-- volatility.sql
-- Computes rolling volatility metrics from daily returns
-- Computes rolling 30-day volatility for each payment network ticker based on daily returns.
-- This serves as a risk / stability metric for comparing Visa vs Mastercard over time.

DROP VIEW IF EXISTS rolling_volatility;

CREATE VIEW rolling_volatility AS
SELECT
  date,
  ticker,
  daily_return,

  -- 30-day rolling volatility (standard deviation of daily returns)
  STDDEV_POP(daily_return) OVER (
    PARTITION BY ticker
    ORDER BY date
    ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
  ) AS rolling_30d_volatility

FROM daily_returns
ORDER BY ticker, date;