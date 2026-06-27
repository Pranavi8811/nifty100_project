import pandas as pd
from pathlib import Path
OUTPUT_DIR = Path("output")

validation_results = []
for file in OUTPUT_DIR.glob("*_clean.csv"):
    df = pd.read_csv(file)

    missing_values = df.isnull().sum().sum()

    validation_results.append({
        "file": file.name,
        "missing_values": missing_values
    })
    validation_df = pd.DataFrame(validation_results)

validation_df.to_csv(
    OUTPUT_DIR / "validation_failures.csv",
    index=False
)

print(validation_df)
print("validation_failures.csv created successfully")