import pandas as pd

df = pd.read_csv("Expenses Export.csv")

print("ANOMALY REPORT")
print("=" * 50)

# Missing paid_by
missing_paid = df[df["paid_by"].isnull()]

for index, row in missing_paid.iterrows():
    print(f"\n[ERROR] Row {index + 1}")
    print("Missing paid_by")
    print("Description:", row["description"])

# Missing currency
missing_currency = df[df["currency"].isnull()]

for index, row in missing_currency.iterrows():
    print(f"\n[WARNING] Row {index + 1}")
    print("Missing currency")
    print("Description:", row["description"])

# Missing split_type
missing_split = df[df["split_type"].isnull()]

for index, row in missing_split.iterrows():
    print(f"\n[WARNING] Row {index + 1}")
    print("Missing split_type")
    print("Description:", row["description"])