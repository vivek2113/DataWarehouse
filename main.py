from extract import extract_data
from transform import transform_data
from load import load_data
from analytics import run_analytics


def main():
    print("===================================")
    print(" DATA WAREHOUSE SYSTEM ")
    print("===================================")

    # Step 1: Extract
    data = extract_data()

    # Step 2: Transform
    transformed_data = transform_data(data)

    # Step 3: Load
    load_data(transformed_data)

    # Step 4: Analytics
    run_analytics()


if __name__ == "__main__":
    main()
