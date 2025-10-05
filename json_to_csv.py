import pandas as pd
import sys
from datetime import datetime
import os

def main(json_path='output.jl', csv_path=None):
    # Generate CSV filename with current date if not provided
    if csv_path is None:
        today_str = datetime.today().strftime('%Y-%m-%d')
        csv_path = f"{today_str}-yc-companies.csv"
    # Check if the input file exists
    if not os.path.isfile(json_path):
        print(f"Error: The file '{json_path}' does not exist.")
        return
    # Read the JSON Lines file
    try:
        df = pd.read_json(json_path, lines=True)
    except Exception as e:
        print(f"Error reading '{json_path}': {e}")
        return
    # Save as CSV
    try:
        df.to_csv(csv_path, index=False)
        print(f"Converted {json_path} to {csv_path}")
    except Exception as e:
        print(f"Error writing '{csv_path}': {e}")

if __name__ == "__main__":
    # Allow optional command-line arguments for input/output files
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()