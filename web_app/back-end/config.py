import os

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")
    HADOOP_HOST = os.getenv("HADOOP_HOST", "http://localhost:9870")
