#!/usr/bin/env bash
set -e

chmod +x install.sh
./install.sh

echo "[INFO] FastAPI app is starting in Docker."
echo "[INFO] Access the API at: http://localhost:8000/tickets"
