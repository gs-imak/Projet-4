# Projet-4
# NOAA Data Analysis Project

## Prerequisites
1. Install Docker and Docker Compose.
2. Install Python 3.8+ and `pip`.
3. (Optional) Install Node.js for frontend.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project
   ```
2. Start Docker containers:
   - Hadoop:
     ```bash
     cd docker/hadoop
     docker-compose up -d
     ```
   - ElasticSearch:
     ```bash
     cd docker/elasticsearch
     docker-compose up -d
     ```

3. Install Python dependencies:
   ```bash
   cd scripts
   pip install -r requirements.txt
   ```

## Running the Application
1. **Download Datasets**:
   ```bash
   python scripts/download_data.py
   ```

2. **Ingest Data**:
   ```bash
   python scripts/data_ingestion.py
   ```

3. **Start the Backend**:
   ```bash
   cd web_app/backend
   python app.py
   ```

4. (Optional) **Start the Frontend**:
   ```bash
   cd web_app/frontend
   npm install
   npm start
   ```

## API Endpoints
1. **Login**:
   ```bash
   curl -X POST http://localhost:5000/auth/login \
        -H "Content-Type: application/json" \
        -d '{"username": "admin", "password": "password"}'
   ```

2. **Query ElasticSearch**:
   ```bash
   curl -X POST http://localhost:5000/elasticsearch/search \
        -H "Authorization: Bearer <JWT_TOKEN>" \
        -H "Content-Type: application/json" \
        -d '{"query": "tornado"}'
   ```

3. **Query Hadoop**:
   ```bash
   curl -X POST http://localhost:5000/hadoop/query \
        -H "Authorization: Bearer <JWT_TOKEN>" \
        -H "Content-Type: application/json" \
        -d '{"file_path": "/data/gsod/2020.csv"}'
   ```

## Verifications
- **Hadoop**: Visit `http://localhost:9870`.
- **ElasticSearch**: Query data via `http://localhost:9200`.
- **Hive**: Query tables using:
   ```bash
   hive
   SELECT * FROM gsod_data LIMIT 10;
   ```
- **HBase**:
   ```bash
   hbase shell
   scan 'storm_events'
   ```

## Shutdown
To stop all containers:
```bash
docker-compose down
```
