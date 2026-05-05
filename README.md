# Docker & CI/CD Pipeline - Main

This repository contains the configuration for containerizing an application and automating its deployment through a CI/CD pipeline.

---

## 🐳 Dockerization

The project uses a **Dockerfile** to ensure the application runs consistently across different environments.

### Commands
* **Build the image:**
    `docker build -t app-name .`
* **Run the container:**
    `docker run -p 8080:8080 app-name`

---

## 🚀 CI/CD Pipeline

The pipeline is automated to handle the lifecycle of the application from code push to deployment.

### Pipeline Stages
1.  **Lint/Test:** Checks code quality and runs unit tests.
2.  **Build:** Creates a production-ready Docker image.
3.  **Push:** Uploads the image to a container registry (e.g., Docker Hub, GHCR).
4.  **Deploy:** Automatically deploys the new image to the server or cluster.

---

## 📁 Repository Structure
* `Dockerfile`: Container configuration.
* `.github/workflows/`: CI/CD pipeline script (YAML).
* `app.py`: Application source code.
