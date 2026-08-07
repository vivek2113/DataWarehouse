import pandas as pd


def transform_data(df):
    """
    Clean and transform the extracted data.
    """

    print("\n===== TRANSFORMING DATA =====")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Create a new column TotalAmount
    df["TotalAmount"] = df["Quantity"] * df["Price"]

    print(df)

    return df


# Testing this file independently
if __name__ == "__main__":
    from extract import extract_data

    data = extract_data()
    transformed_data = transform_data(data)
