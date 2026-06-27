import pandas as pd
import sqlite3

conn = sqlite3.connect("../../db/nifty100.db")

df = pd.read_excel("../../data/stock_prices.xlsx")

# Keep only required columns
df = df[["company_id", "date", "close_price"]]

# Rename to match database schema
df = df.rename(columns={
    "date": "price_date"
})

print(df.head())
print("Rows:", len(df))

df.to_sql(
    "stock_prices",
    conn,
    if_exists="append",
    index=False
)

print("Stock Prices loaded successfully")

conn.close()