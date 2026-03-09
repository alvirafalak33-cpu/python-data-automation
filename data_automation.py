import os
import pandas as pd

folder = "data_files"
report = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path)
        rows = len(df)
        report.append({"file": file, "rows": rows})

summary = pd.DataFrame(report)
summary.to_csv("report_summary.csv", index=False)

print("Report generated successfully.")
