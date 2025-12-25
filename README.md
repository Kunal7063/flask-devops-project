# Flask DevOps App

Simple Flask application containerised using Docker.

## Tech Stack
- Python
- Flask
- Docker

## How to Run (Docker)

```bash
docker build -t flask-devops-app .
docker run -d -p 5000:5000 flask-devops-app
