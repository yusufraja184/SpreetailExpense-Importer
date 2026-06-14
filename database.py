import sqlite3

conn = sqlite3.connect("expenses.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    description TEXT,
    paid_by TEXT,
    amount REAL,
    currency TEXT,
    split_type TEXT,
    split_with TEXT,
    split_details TEXT,
    notes TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")