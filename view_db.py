import sqlite3
import pandas as pd

conn = sqlite3.connect("expenses.db")

df = pd.read_sql_query(
    "SELECT * FROM expenses LIMIT 10",
    conn
)

print(df)

conn.close()