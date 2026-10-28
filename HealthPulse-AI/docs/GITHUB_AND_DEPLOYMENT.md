# GitHub and deployment status

## Published source

Full HealthPulse AI source:
https://github.com/harshakavali81-collab/harshavardhan-portfolio/tree/main/HealthPulse-AI

Portfolio case study:
https://harshakavali81-collab.github.io/harshavardhan-portfolio/cases/healthpulse.html

GitHub Pages publishes only the static case study. It does not host the FastAPI/React application.

## Optional dedicated repository

Create an empty repository named HealthPulse-AI on GitHub, then from an extracted project directory:

```bash
git init
git branch -M main
git add .
git commit -m "Initial HealthPulse AI full-stack release"
git remote add origin https://github.com/harshakavali81-collab/HealthPulse-AI.git
git push -u origin main
```

Authenticate with a supported GitHub login method. Do not commit tokens or passwords.

## Local Docker startup

```bash
cp .env.example .env
docker compose up --build
```

Dashboard: http://localhost:8080
API docs: http://localhost:8000/docs

## Production requirements (not claimed)

Public API/React hosting, HTTPS and DNS, authentication, rate limiting, backups, logging, source refresh monitoring, source-schema validation, and independently validated epidemiology models all need real infrastructure and expert review.