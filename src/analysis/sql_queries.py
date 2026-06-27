import sqlite3
import pandas as pd

conn = sqlite3.connect("../../db/nifty100.db")
query = """
SELECT
    company_id,
    COUNT(annual_report) AS total_reports
FROM documents
GROUP BY company_id
ORDER BY total_reports DESC;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()