import pandas as pd
from sklearn.cluster import KMeans

print(" Clustering started")

df = pd.read_csv("data_preprocessed.csv")

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(df)

# Count samples per cluster
counts = df["cluster"].value_counts()

with open("clusters.txt", "w") as f:
    f.write(str(counts))

print(" clusters.txt created")
