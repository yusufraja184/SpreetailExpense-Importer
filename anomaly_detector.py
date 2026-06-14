import pandas as pd

df = pd.read_csv("Expenses Export.csv")

anomalies = []

# Missing paid_by
for index, row in df[df["paid_by"].isnull()].iterrows():
    anomalies.append(
        f"ERROR | Row {index+1} | Missing paid_by | {row['description']}"
    )

# Missing currency
for index, row in df[df["currency"].isnull()].iterrows():
    anomalies.append(
        f"WARNING | Row {index+1} | Missing currency | {row['description']}"
    )

# Missing split_type
for index, row in df[df["split_type"].isnull()].iterrows():
    anomalies.append(
        f"WARNING | Row {index+1} | Missing split_type | {row['description']}"
    )

print("IMPORT REPORT")
print("=" * 50)

for item in anomalies:
    print(item)

with open("reports/import_report.txt", "w") as file:
    file.write("IMPORT REPORT\n")
    file.write("=" * 50 + "\n")

    for item in anomalies:
        file.write(item + "\n")

print("\nReport saved to reports/import_report.txt")