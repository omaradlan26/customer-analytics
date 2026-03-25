import pandas as pd
from sklearn.preprocessing import StandardScaler

print("🚀 Preprocessing started")

df = pd.read_csv("data_raw.csv")

# اطبع الأعمدة عشان نتأكد
print("Columns:", df.columns)

# تنظيف
df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))

# تنظيف أسماء الأعمدة (مهم جدًا)
df.columns = df.columns.str.strip()

# Encode كل الأعمدة النصية تلقائي
df = pd.get_dummies(df, drop_first=True)

# Scaling
scaler = StandardScaler()
num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

# Save
df.to_csv("data_preprocessed.csv", index=False)

print("✅ data_preprocessed.csv created")