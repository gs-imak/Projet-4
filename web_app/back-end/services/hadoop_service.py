import requests
from config import Config

def query_hadoop(file_path):
    url = f"{Config.HADOOP_HOST}/webhdfs/v1/{file_path}?op=OPEN"
    response = requests.get(url)
    if response.status_code == 200:
        return {"file_content": response.text}
    return {"error": "File not found or inaccessible"}
