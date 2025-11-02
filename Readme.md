# ThreatForge: Threat Intelligence Aggregation and Scoring Platform

## Overview
ThreatForge aggregates Indicators of Compromise (IOCs) from multiple threat intelligence APIs, computes composite risk scores, and presents the data in an interactive Flask dashboard.

## Features
- Integrates VirusTotal, AbuseIPDB, AlienVault OTX, GreyNoise APIs for IOC data
- Normalizes and correlates IOC reputation and details
- Calculates weighted risk scores and color-codes results
- Provides search, alerts, analytics charts, and export functionality
- REST API endpoint for external integrations
- Automated data fetching with Celery scheduler
- JWT-secured dashboard access

## Prerequisites
- Python 3.9+
- MongoDB (local or cloud)
- Redis (for Celery task queue)
- API keys for integrated threat feeds

## Setup and Run
1. Clone the repo
2. Create `.env` file with your API keys and config variables
3. Install dependencies: `pip install -r requirements.txt`
4. Run MongoDB and Redis services
5. Start Flask app: `python run.py`
6. Access dashboard at `http://localhost:5000/dashboard`

## Docker Usage
docker build -t threatforge .
docker run -p 5000:5000 threatforge


## License
MIT License