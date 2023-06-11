A simple API to manage articles that suitable for developing a blog using FastAPI, includes the workflow spec to deploy the app onto DigitalOcean Droplet.

# How to run
## Pre-requisites:
 - Docker

---

## Run as Docker container:
```
docker build -t api-article .
docker run --rm -d -p 8000:80 --name api-article api-article
```
---
