# DATASCI 209 Final Project

## Exploring Life Expectancy: Beyond GDP
This is a Flask web app for a project exploring factors that influence life expectancy beyond GDP.

Created by Jagriti Singh, Mina Baghai, Shane Brooks, and Taylor DeSantis.

## Run with Docker Compose

This repository includes a minimal `docker-compose.yml` so you can run the app in a container without creating a Dockerfile.

From the project root (where `docker-compose.yml` is located) you can start the app with:

```powershell
# foreground (use when developing or to watch logs)
docker compose up

# detached (run in background)
docker compose up -d

# stop and remove containers
docker compose down

# follow logs for the service named "web"
docker compose logs -f web
```

Notes:
- The compose file uses the official Python image and runs `pip install -r requirements.txt` inside the container on first start, then runs Gunicorn on port 8080. The service maps host port 8080 to the container, so open http://localhost:8080 in your browser.
- If your environment uses the older binary, `docker-compose` (with a hyphen) will also work (e.g., `docker-compose up -d`).
- If you use Podman in WSL, install `podman-compose` or use the newer `podman compose` command and then run the same commands (replace `docker compose` with `podman-compose` or `podman compose`).

If you want a build-based workflow (faster repeated starts, cached dependencies), I can add a simple `Dockerfile` and update the compose file to build an image instead of installing requirements at runtime.
