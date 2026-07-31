# Lightweight DevOps System Monitoring API 🚀

A modern, containerized REST API built with **Python (FastAPI)** and **Docker** that exposes real-time system performance metrics (CPU, Memory, and Disk usage).

This project demonstrates a production-ready combination of **backend development** and **infrastructure containerization**.

---

## 🛠️ Tech Stack & Key Features

- **FastAPI**: High-performance, modern web framework for building APIs with Python 3.10+.
- **Docker**: Fully containerized using a lightweight `python:3.10-slim` image to minimize footprint.
- **psutil**: Cross-platform library for retrieving live hardware metrics.
- **Auto-generated Docs**: Native interactive Swagger UI documentation.

---

## 📁 Project Structure

```text
├── Dockerfile          # Docker build configuration
├── main.py             # FastAPI application source code
├── requirements.txt    # Python application dependencies
└── README.md           # Documentation
```

---

## ⚡ Quick Start (Using Docker)

Ensure [Docker](https://docker.com) is installed on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/Landry5545/devops-monitoring-api.git
cd devops-monitoring-api
```

### 2. Build the Docker image
```bash
docker build -t sys-monitoring-api .
```

### 3. Run the container
```bash
docker run -d -p 8000:8000 --name monitoring-app sys-monitoring-api
```

---

## 📊 API Endpoints & Usage

Once the container is running, open your browser or use `curl`:

### 🔍 Live system metrics
- **URL**: `http://localhost:8000/metrics`
- **Method**: `GET`
- **Sample response**:
```json
{
  "cpu_usage_percent": 12.5,
  "memory": {
    "total_gb": 16.0,
    "available_gb": 7.42,
    "used_percent": 53.6
  },
  "disk": {
    "total_gb": 465.76,
    "free_gb": 120.34,
    "used_percent": 74.2
  }
}
```

### 📋 Interactive API documentation
FastAPI auto-generates interactive docs, testable directly from the browser:
- **Swagger UI**: `http://localhost:8000/docs`

---

## 🔧 Future Roadmap
- [ ] Integrate a **Prometheus** metrics exporter format.
- [ ] Connect a **Grafana** dashboard to visualize live hardware changes.
- [ ] Implement token-based authentication for secure monitoring.

---

---

## 🔍 Deployment Note
When deploying this container on a host with custom iptables rules (e.g. a 
`DOCKER-USER` chain used to restrict Docker's default traffic bypass of UFW), 
remember to explicitly allow the container's port:

    sudo iptables -I DOCKER-USER -p tcp --dport 8000 -j ACCEPT

Without this, the container will respond to `localhost` requests but be 
unreachable from other hosts on the network, since Docker's forwarded 
traffic passes through the `FORWARD` chain rather than `INPUT`.

💡 *Developed as a portfolio showcase combining systems engineering and software development.*
