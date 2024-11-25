from elasticsearch import Elasticsearch
from config import Config

es = Elasticsearch(Config.ELASTICSEARCH_HOST)

def query_elasticsearch(query):
    index = "gsod_data"
    search_body = {
        "query": {
            "match": {
                "description": query
            }
        }
    }
    response = es.search(index=index, body=search_body)
    return {"hits": [hit["_source"] for hit in response["hits"]["hits"]]}
