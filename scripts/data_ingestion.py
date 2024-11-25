import os
from hdfs import InsecureClient
from pyhive import hive
import happybase
import csv

# Hadoop and Hive configuration
HDFS_URL = "http://localhost:9870"  # Replace with your NameNode URL
HDFS_USER = "hadoop"
HIVE_HOST = "localhost"
HBASE_HOST = "localhost"

# Define paths
HDFS_BASE_PATH = "/data"

# Connect to Hadoop HDFS
hdfs_client = InsecureClient(HDFS_URL, user=HDFS_USER)

# Connect to Hive
hive_conn = hive.Connection(host=HIVE_HOST, port=10000, username=HDFS_USER)

# Connect to HBase
hbase_conn = happybase.Connection(HBASE_HOST)


def upload_to_hdfs(local_path, hdfs_path):
    """
    Uploads a file or directory to HDFS.
    """
    if os.path.isfile(local_path):
        hdfs_client.upload(hdfs_path, local_path, overwrite=True)
        print(f"Uploaded {local_path} to HDFS at {hdfs_path}")
    elif os.path.isdir(local_path):
        for root, _, files in os.walk(local_path):
            for file in files:
                full_local_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_local_path, local_path)
                full_hdfs_path = os.path.join(hdfs_path, relative_path)
                hdfs_client.upload(full_hdfs_path, full_local_path, overwrite=True)
                print(f"Uploaded {full_local_path} to HDFS at {full_hdfs_path}")


def create_hive_table(query):
    """
    Executes a HiveQL query to create a table.
    """
    with hive_conn.cursor() as cursor:
        cursor.execute(query)
        print("Hive table created successfully.")


def load_hive_data(hive_table, hdfs_path):
    """
    Loads data into a Hive table from HDFS.
    """
    query = f"LOAD DATA INPATH '{hdfs_path}' INTO TABLE {hive_table}"
    with hive_conn.cursor() as cursor:
        cursor.execute(query)
        print(f"Data loaded into Hive table {hive_table} from {hdfs_path}")


def create_hbase_table(table_name, column_families):
    """
    Creates a table in HBase.
    """
    hbase_admin = hbase_conn.open()
    if table_name not in hbase_admin.tables():
        hbase_admin.create_table(
            table_name, {cf: dict() for cf in column_families}
        )
        print(f"HBase table {table_name} created with column families {column_families}")


def load_hbase_data(table_name, data_path):
    """
    Loads data into an HBase table from a CSV file.
    """
    table = hbase_conn.table(table_name)
    with open(data_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_key = row.get('event_id') or row.get('id')  # Adjust for specific dataset
            table.put(
                row_key,
                {f"cf:{k}": v for k, v in row.items() if k != "event_id"}
            )
    print(f"Data loaded into HBase table {table_name} from {data_path}")


if __name__ == "__main__":
    # Paths to local data
    local_gsod_path = "../data/gsod/"
    local_isd_path = "../data/isd/"
    local_storm_events_path = "../data/storm_events/decompressed/"
    local_metar_path = "../data/metar_reports/"

    # HDFS destinations
    hdfs_gsod_path = f"{HDFS_BASE_PATH}/gsod/"
    hdfs_isd_path = f"{HDFS_BASE_PATH}/isd/"
    hdfs_storm_events_path = f"{HDFS_BASE_PATH}/storm_events/"
    hdfs_metar_path = f"{HDFS_BASE_PATH}/metar/"

    # Upload data to HDFS
    print("Uploading GSOD data to HDFS...")
    upload_to_hdfs(local_gsod_path, hdfs_gsod_path)

    print("Uploading ISD data to HDFS...")
    upload_to_hdfs(local_isd_path, hdfs_isd_path)

    print("Uploading Storm Events data to HDFS...")
    upload_to_hdfs(local_storm_events_path, hdfs_storm_events_path)

    print("Uploading METAR data to HDFS...")
    upload_to_hdfs(local_metar_path, hdfs_metar_path)

    # Create Hive tables
    print("Creating Hive tables...")
    create_hive_table("""
        CREATE TABLE IF NOT EXISTS gsod_data (
            station STRING,
            date STRING,
            temp DOUBLE,
            wind_speed DOUBLE,
            precipitation DOUBLE
        )
        ROW FORMAT DELIMITED
        FIELDS TERMINATED BY ','
        STORED AS TEXTFILE
    """)
    create_hive_table("""
        CREATE TABLE IF NOT EXISTS isd_data (
            station STRING,
            date STRING,
            temp DOUBLE,
            wind_speed DOUBLE,
            pressure DOUBLE
        )
        ROW FORMAT DELIMITED
        FIELDS TERMINATED BY ','
        STORED AS TEXTFILE
    """)

    # Load data into Hive tables
    print("Loading data into Hive tables...")
    load_hive_data("gsod_data", hdfs_gsod_path)
    load_hive_data("isd_data", hdfs_isd_path)

    # Create HBase table
    print("Creating HBase table for Storm Events...")
    create_hbase_table("storm_events", ["details", "metadata"])

    # Load data into HBase
    print("Loading Storm Events data into HBase...")
    for file in os.listdir(local_storm_events_path):
        if file.endswith(".csv"):
            load_hbase_data("storm_events", os.path.join(local_storm_events_path, file))

    print("Data ingestion complete!")
