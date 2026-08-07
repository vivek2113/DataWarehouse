import sqlite3

def load_data(df):
    """
    Load transformed data into SQLite database.
    """

    print("\n===== LOADING DATA INTO DATABASE =====")

    # Connect to SQLite database
    conn = sqlite3.connect("warehouse.db")

    # Store DataFrame as a table
    df.to_sql("Sales", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("Data loaded successfully into warehouse.db")


# Test this file independently
if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    data = extract_data()
    transformed_data = transform_data(data)

    load_data(transformed_data)
