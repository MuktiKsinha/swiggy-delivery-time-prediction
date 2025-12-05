import pandas as pd
import requests
from pathlib import Path

# path for data
root_path = Path(__file__).parent.parent
data_path = root_path / "data" / "raw" / "swiggy.csv"

# prediction endpoint
predict_url = "http://127.0.0.1:8000/predict"

# sample row
sample_row = pd.read_csv(data_path).dropna().sample(1)
target_value = sample_row.iloc[:, -1].values.item().replace("(min) ", "")
print("Actual target:", target_value)

# remove target
data = (
    sample_row
    .drop(columns=[sample_row.columns[-1]])
    .squeeze()
    .to_dict()
)

response = requests.post(predict_url, json=data)

print("Status:", response.status_code)

if response.status_code == 200:
    print("Predicted:", float(response.text), "min")
else:
    print("Error:", response.json())
