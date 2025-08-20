#!/bin/bash
set -e
echo "Starting app ..."
docker-compose up -d

echo "Waiting a few seconds for DB to initialize..."
sleep 5

echo "Application is (or will be) available at: http://localhost:5000"
docker-compose ps
