# CloudLab Secure API

A containerized FastAPI application demonstrating DevOps and security best practices.

---

## 🚀 Features

- Docker containerization
- Non-root container execution (security hardening)
- Environment-based configuration
- docker-compose orchestration
- Health check endpoint
- Clean build layers with `.dockerignore`

---

## 🏗 Architecture

Client → Docker Compose → FastAPI Container → Uvicorn

---

## 🔐 Security Practices Implemented

- Runs as non-root user
- Explicit port exposure
- Environment variable injection
- Minimal base image (`python:3.11-slim`)
- Clean dependency installation with `--no-cache-dir`

---

## 🧪 Run Locally

```bash
docker compose up --build# deploy trigger Wed Feb 18 19:59:56 CST 2026
# deploy trigger 2026-02-18T20:06:44-06:00
