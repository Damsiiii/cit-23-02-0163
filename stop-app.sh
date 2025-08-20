#!/bin/bash
set -e
echo "Stopping app (containers stopped, data preserved) ..."
docker-compose stop
echo "Stopped. Persistent data remains in Docker volume 'db_data'."
