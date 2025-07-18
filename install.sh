#!/usr/bin/env bash
set -e

if ! command -v docker >/dev/null 2>&1; then
  echo "[ERROR] Docker is not installed. Please install Docker and try again."
  exit 1
fi

echo "[INFO] Building Docker image..."
docker-compose build

echo "[INFO] Starting Docker containers..."
docker-compose up -d

echo "[INFO] Environment setup complete."
