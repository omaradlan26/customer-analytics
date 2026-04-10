import sys
import pandas as pd

print(" Ingest started")

# read dataset (Mall_Customers.csv)
df = pd.read_csv(sys.argv[1])

# save raw copy
df.to_csv("data_raw.csv", index=False)

print(" data_raw.csv created successfully")
