#!/bin/bash
set -e
echo "Preparing app ..."

# create network if not exists
docker network inspect myapp-network >/dev/null 2>&1 || \
  docker network create myapp-network

# create named volume for persistence
docker volume inspect db_data >/dev/null 2>&1 || \
  docker volume create db_data

# build custom images (web)
docker-compose build

echo "Preparation complete."
