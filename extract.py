import pandas as pd

def extract_data():
    """
    Extract data from the CSV file.
    """

    df = pd.read_csv("sales.csv")

    print("\n===== EXTRACTED DATA =====")
    print(df)

    return df


if __name__ == "__main__":
    extract_data()
