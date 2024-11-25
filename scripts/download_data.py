import os
import requests
from tqdm import tqdm
import gzip
import shutil


def download_file(url, dest_folder):
    """
    Downloads a file from the specified URL to the destination folder.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    local_filename = os.path.join(dest_folder, url.split("/")[-1])

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        with open(local_filename, 'wb') as f, tqdm(
            desc=f"Downloading {url.split('/')[-1]}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
                bar.update(len(chunk))

    print(f"Downloaded: {local_filename}")
    return local_filename


def decompress_gz_files(source_folder, dest_folder):
    """
    Decompresses .gz files in the source folder to the destination folder.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file_name in os.listdir(source_folder):
        if file_name.endswith(".gz"):
            source_file = os.path.join(source_folder, file_name)
            dest_file = os.path.join(dest_folder, file_name[:-3])  # Remove .gz extension
            with gzip.open(source_file, 'rb') as f_in:
                with open(dest_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            print(f"Decompressed: {dest_file}")


def download_gsod_data(years, dest_folder):
    """
    Downloads NOAA GSOD data for specified years.
    """
    base_url = "https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/"
    for year in years:
        year_url = f"{base_url}{year}/"
        try:
            response = requests.get(year_url)
            response.raise_for_status()
            # Parse the HTML response to find CSV files
            for line in response.text.splitlines():
                if ".csv" in line:  # Assuming CSV files are present in the HTML listing
                    file_name = line.split('href="')[1].split('"')[0]
                    file_url = f"{year_url}{file_name}"
                    download_file(file_url, dest_folder)
        except Exception as e:
            print(f"Error downloading GSOD data for year {year}: {e}")


def download_isd_data(years, dest_folder):
    """
    Downloads NOAA Integrated Surface Database (ISD) data for specified years.
    """
    base_url = "https://www.ncei.noaa.gov/data/global-hourly/access/"
    for year in years:
        year_url = f"{base_url}{year}/"
        try:
            response = requests.get(year_url)
            response.raise_for_status()
            # Parse the HTML response to find CSV files
            for line in response.text.splitlines():
                if ".csv" in line:  # Assuming CSV files are present in the HTML listing
                    file_name = line.split('href="')[1].split('"')[0]
                    file_url = f"{year_url}{file_name}"
                    download_file(file_url, dest_folder)
        except Exception as e:
            print(f"Error downloading ISD data for year {year}: {e}")


def download_storm_events_data(years, dest_folder):
    """
    Downloads NOAA Storm Events data for specified years.
    """
    base_url = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
    for year in years:
        file_url = f"{base_url}StormEvents_details-ftp_v1.0_{year}.csv.gz"
        try:
            download_file(file_url, dest_folder)
        except Exception as e:
            print(f"Error downloading Storm Events data for year {year}: {e}")


def download_metar_data(dest_folder):
    """
    Downloads NOAA METAR text reports.
    """
    base_url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        # Extract file names from HTML content and download
        for line in response.text.splitlines():
            if ".TXT" in line:  # Assuming METAR files have .TXT extension
                file_url = f"{base_url}{line.split()[-1]}"
                download_file(file_url, dest_folder)
    except Exception as e:
        print(f"Error downloading METAR data: {e}")


if __name__ == "__main__":
    # Define destination folders
    data_folders = {
        "gsod": "../data/gsod/",
        "isd": "../data/isd/",
        "storm_events": "../data/storm_events/",
        "metar_reports": "../data/metar_reports/",
    }

    # Define years of interest
    gsod_years = range(2020, 2025)  # GSOD: 2020-2024 inclusive
    isd_years = range(2020, 2025)  # ISD: 2020-2024 inclusive
    storm_events_years = range(2020, 2025)  # Storm Events: 2020-2024

    # Download datasets
    print("Downloading GSOD data...")
    download_gsod_data(gsod_years, data_folders["gsod"])

    print("Downloading ISD data...")
    download_isd_data(isd_years, data_folders["isd"])

    print("Downloading Storm Events data...")
    download_storm_events_data(storm_events_years, data_folders["storm_events"])

    print("Decompressing Storm Events data...")
    decompress_gz_files(data_folders["storm_events"], f"{data_folders['storm_events']}/decompressed")

    print("Downloading METAR data...")
    download_metar_data(data_folders["metar_reports"])

    print("All downloads and decompression complete!")
