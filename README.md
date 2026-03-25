# LeakSentinel – Dark Web Monitoring Tool (Simulation)

## Overview
LeakSentinel is a backend system that simulates monitoring of breach data and alerts users when sensitive information matches predefined keywords.

## Features
- Breach data ingestion (simulated)
- Email, username, hash extraction
- Keyword monitoring
- Alert generation
- REST API access
- Scheduled scanning

## Setup

### 1. Clone repo

git clone <repo>
cd backend


### 2. Install dependencies

pip install -r requirements.txt


### 3. Configure environment
Create `.env` file

### 4. Run MongoDB

mongod


### 5. Start server

uvicorn app.main:app --reload


## API Endpoints
- POST /keywords
- GET /keywords
- DELETE /keywords/{value}
- GET /breach-data
- GET /alerts
- POST /run-scan

## Ethics
This project uses simulated data only. Do NOT use for illegal scraping or unauthorized monitoring.

## License
MIT