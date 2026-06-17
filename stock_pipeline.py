import yfinance as yf
import pyodbc
from azure.identity import InteractiveBrowserCredential
import struct 

server = "your-azure-server.database.windows.net"  # REPLACE WITH YOUR SERVER NAME
database = "StockDataDB"

credential = InteractiveBrowserCredential()
token = credential.get_token("https://database.windows.net/.default")
token_bytes = token.token.encode("UTF-16-LE")
token_struct = struct.pack(f"<I{len(token_bytes)}s", len(token_bytes), token_bytes)

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Encrypt=yes;",
    attrs_before={1256: token_struct}
)

cursor = conn.cursor()

tickers = ["MSFT", "LCID", "WFC", "BAC"]

for ticker in tickers:
    data = yf.download(ticker, start="2020-01-01", auto_adjust=True, progress=False)
    data.columns = data.columns.get_level_values(0)
    data.reset_index(inplace=True)
    inserted = 0
    for _, row in data.iterrows():
        cursor.execute("""
            IF NOT EXISTS (SELECT 1 FROM STOCK_MARKET_DATA WHERE Date = ? AND TickerSymbol = ?)
            INSERT INTO STOCK_MARKET_DATA (Date, [Close], TickerSymbol)
            VALUES (?, ?, ?)
        """, row["Date"], ticker, row["Date"], float(row["Close"]), ticker)
        inserted += 1
    conn.commit()
    print(f"{ticker}: {inserted} rows processed")

print("Done")
