-- raw_market_prices.sql
-- Defines schema for raw market price data loaded from external sources (e.g. Yahoo Finance)
-- for payment network equities (Visa, Mastercard, S&P 500).
-- This table stores unmodified, ingestion-level price data and serves as the raw input layer for
-- downstream analytics (daily returns, volatility, indexed performance, etc.).
-- Data in this table is intentionally kept close to source format. Any cleaning, normalization,
-- or derived metrics should be handled in separate schema / analytics layers.

DROP TABLE IF EXISTS raw_market_prices;

CREATE TABLE IF NOT EXISTS raw_market_prices (
  date DATE,
  ticker VARCHAR(10),
  adj_close DECIMAL(12,4)
);