import pandas as pd

print("🚀 Analytics started")

df = pd.read_csv("data_preprocessed.csv")

# Insight 1
insight1 = f"Number of rows: {df.shape[0]}"

# Insight 2
insight2 = f"Number of columns: {df.shape[1]}"

# Insight 3 (strong extra insight)
insight3 = f"Average values:\n{df.mean().to_string()}"

# Save insights
with open("insight1.txt", "w") as f:
    f.write(insight1)

with open("insight2.txt", "w") as f:
    f.write(insight2)

with open("insight3.txt", "w") as f:
    f.write(insight3)

print("✅ Insights saved")