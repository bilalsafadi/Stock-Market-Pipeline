# Stock Market Financial Data Pipeline

This is my automated data pipeline that ingests live stock market data into a cloud database and visualizes it through an interactive dashboard.

## Tech Stack
- **Python** — automated data ingestion using yfinance API
- **Azure SQL** — cloud-hosted database
- **Power BI** — interactive dashboard with independent axis scaling per ticker
- **SSMS** — database management and query execution

## Features
- Pulls live stock data for tickers MSFT, LCID, WFC, and BAC
- Safe to run daily without duplicating data
- Resolved reserved SQL keyword conflicts during data ingestion
- Interactive Power BI dashboard with independent y-axis scaling per ticker

## How It Works
1. Python script pulls stock data from Yahoo Finance via yfinance API
2. Data is inserted into Azure SQL cloud database
3. Power BI connects directly to Azure SQL and visualizes price history
4. Dashboard allows filtering by ticker symbol with auto-scaling axes

## Stocks Currently Tracked
| Ticker | Company |
|--------|---------|
| MSFT | Microsoft |
| LCID | Lucid Motors |
| WFC | Wells Fargo |
| BAC | Bank of America |
