# cit-23-02-0163
Assignment 1 for Virtualization and containers
#CIT-23-02-0163 - Docker Flask + MySQL App

## Deployment Requirements
- Docker (Engine) installed
- Docker Compose (v2 or v1) — `docker-compose` or `docker compose` available

## What the application does
A simple Flask web app that stores a visit count in a MySQL database. The DB data is persisted in the Docker named volume `db_data`.

## Network & Volumes
- Network: myapp-network (Docker network created by prepare script)
- Volume: db_data -> /var/lib/mysql (persistent storage for MySQL)

## Containers
- myapp-web: Flask application serving HTTP on port 5000
- myapp-db: MySQL server listening on port 3306

## How to run (example workflow)
1. Prepare: `./prepare-app.sh`
2. Start: `./start-app.sh`
   - App URL: http://localhost:5000
3. Stop (preserve data): `./stop-app.sh`
4. Remove all resources (delete data too): `./remove-app.sh`

## Example usage to verify persistence
1. `./start-app.sh`
2. Open http://localhost:5000 — note the visit count
3. `./stop-app.sh`
4. `./start-app.sh`
5. Re-open http://localhost:5000 — count continues from previous value (data persisted)

## Notes
- Change host port mapping in docker-compose if ports conflict.
