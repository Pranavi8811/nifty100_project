import pandas as pd
import sqlite3

conn = sqlite3.connect("../../db/nifty100.db")

df = pd.read_csv("../../output/stock_prices_clean.csv")

df = df.rename(columns={
    "abb": "company_id",
    df.columns[2]: "price_date",
    df.columns[6]: "close_price"
})

df = df[["company_id", "price_date", "close_price"]]

df.to_sql("stock_prices", conn, if_exists="append", index=False)

print("Stock prices data loaded successfully")

conn.close()