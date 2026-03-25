import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("🚀 Visualization started")

df = pd.read_csv("data_preprocessed.csv")

# 1. Histogram
df.hist(figsize=(10,8))

# 2. Correlation heatmap
plt.figure()
sns.heatmap(df.corr(), annot=False)

# Save all plots
plt.savefig("summary_plot.png")

print("✅ summary_plot.png created")