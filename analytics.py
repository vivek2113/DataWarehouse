import sqlite3
import pandas as pd


def run_analytics():
    # Connect to the database
    conn = sqlite3.connect("warehouse.db")

    print("\n===== DATA WAREHOUSE ANALYTICS =====\n")

    # Read data from Sales table
    df = pd.read_sql_query("SELECT * FROM Sales", conn)

    # 1. Total Sales Amount
    total_sales = df["TotalAmount"].sum()
    print("Total Sales Amount :", total_sales)

    # 2. Total Quantity Sold
    total_quantity = df["Quantity"].sum()
    print("Total Quantity Sold :", total_quantity)

    # 3. Sales by Category
    print("\nSales by Category")
    print(df.groupby("Category")["TotalAmount"].sum())

    # 4. Sales by Customer
    print("\nSales by Customer")
    print(df.groupby("Customer")["TotalAmount"].sum())

    conn.close()


if __name__ == "__main__":
    run_analytics()
