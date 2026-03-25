# Customer Analytics Pipeline

## Team Members
- Your Name

## Build
docker build -t customer-analytics .

## Run
docker run -it -v "%cd%":/app/pipeline customer-analytics

## Execution Flow
ingest.py → preprocess.py → analytics.py → visualize.py → cluster.py

## Output Files
- data_raw.csv
- data_preprocessed.csv
- insight1.txt
- insight2.txt
- insight3.txt
- summary_plot.png
- clusters.txt"# customer-analytics" 
