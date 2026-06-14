# import pandas as pd

# df = pd.read_csv("Expenses Export.csv")

# print("Rows:", df.shape[0])
# print("Columns:", df.shape[1])

# print("\nColumn Names:")
# print(df.columns)

# print("\nData Types:")
# print(df.dtypes)

# print("\nMissing Values:")
# print(df.isnull().sum())

# ////// Data profiling  //////.......
# ....here we got paid_by 1, currency 1, split_type 1, split_details 36, notes 22......
# .... ie. One expense has no payer.,   One expense has no currency., 
# .... One row doesn't tell us how the expense is divided......




#  //  anomaly detection  //////

# import pandas as pd

# df = pd.read_csv("Expenses Export.csv")

# print("Rows with missing paid_by:")
# print(df[df["paid_by"].isnull()])

# print("\nRows with missing currency:")
# print(df[df["currency"].isnull()])

# print("\nRows with missing split_type:")
# print(df[df["split_type"].isnull()])          #  we found 3 anomalies.....





#   Combined code...............................
import pandas as pd

df = pd.read_csv("Expenses Export.csv")

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())