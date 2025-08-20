#!/bin/bash
set -e
echo "Removing app and resources ..."

# Bring everything down and remove images and volumes created by compose
docker-compose down --rmi all --volumes --remove-orphans

# Remove network if present
docker network rm myapp-network 2>/dev/null || true

echo "Removed app. Note: 'db_data' volume should be removed by the --volumes flag above."
