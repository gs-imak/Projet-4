from pyhive import hive
import os

# Hive connection details
HIVE_HOST = "localhost"
HIVE_PORT = 10000
HIVE_USER = "hadoop"

def load_data_into_hive():
    # Connect to Hive
    conn = hive.Connection(host=HIVE_HOST, port=HIVE_PORT, username=HIVE_USER)
    cursor = conn.cursor()

    # Specify the path to the data
    data_path = "/path/to/gsod.csv"

    # Hive LOAD DATA command
    load_query = f"""
    LOAD DATA LOCAL INPATH '{data_path}'
    INTO TABLE gsod
    PARTITION (year=2020, month=1);
    """

    try:
        # Execute the query
        cursor.execute(load_query)
        print("Data successfully loaded into Hive.")
    except Exception as e:
        print(f"Error loading data: {e}")

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_data_into_hive()
