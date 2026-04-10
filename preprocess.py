import pandas as pd
from sklearn.preprocessing import StandardScaler

print(" Preprocessing started")

df = pd.read_csv("data_raw.csv")

print("Columns:", df.columns)

df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))

df.columns = df.columns.str.strip()

df = pd.get_dummies(df, drop_first=True)

scaler = StandardScaler()
num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

df.to_csv("data_preprocessed.csv", index=False)

print(" data_preprocessed.csv created")
