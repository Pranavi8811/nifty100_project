import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)

for file in DATA_DIR.glob("*.xlsx"):

    try:
        df = pd.read_excel(file, header=1)

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
        )

        df = df.drop_duplicates()

        print(f"Processing: {file.name}")

        output_file = OUTPUT_DIR / f"{file.stem}_clean.csv"

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file.name}")

    except Exception as e:
        print(f"Error processing {file.name}: {e}")