import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("Expenses Export.csv")

# Connect database
conn = sqlite3.connect("expenses.db")

# Remove rows with critical errors
valid_df = df.dropna(subset=["paid_by"])

# Add status column
valid_df["status"] = "valid"

# Save to database
valid_df.to_sql(
    "expenses",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print(f"{len(valid_df)} records imported successfully")