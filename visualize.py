import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(" Visualization started")

df = pd.read_csv("data_preprocessed.csv")

df.hist(figsize=(10,8))

plt.figure()
sns.heatmap(df.corr(), annot=False)

plt.savefig("summary_plot.png")

print(" summary_plot.png created")
