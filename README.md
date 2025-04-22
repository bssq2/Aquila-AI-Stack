# Aquila AI Stack

A boilerplate microservices stack for data collection, model inference, dashboarding, and security management.

## 🏗 Architecture

- **data-collector** (port 5000)  
  - A simple Flask service that fetches or simulates external data.
- **ml-model** (port 6000)  
  - A Python service exposing a classifier endpoint.
- **fin-dash** (port 7000)  
  - A Dash‐based financial dashboard UI.
- **sec-manager** (port 9000)  
  - A Flask service handling authentication and middleware.

Each service lives in its own Docker container, and you’ll find corresponding Helm charts for Kubernetes.

## 🚀 Quickstart

### Prerequisites

- Docker & Docker Compose  
- (Optional) Helm & Kubernetes  
- Python 3.9+ (for local development)

### Environment Variables

Copy the example `.env.example` to `.env` and fill in any secrets:

```bash
cp .env.example .env
# Edit JWT_SECRET, DB credentials, API keys, etc.