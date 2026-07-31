from fastapi import FastAPI
import psutil
import datetime

app = FastAPI(title="DevOps Monitoring API", version="1.0")


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the DevOps Monitoring API",
        "status": "Healthy",
        "timestamp": datetime.datetime.now().isoformat()
    }


@app.get("/metrics")
def get_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu_usage_percent": cpu_usage,
        "memory": {
            "total_gb": round(memory.total / (1024 ** 3), 2),
            "available_gb": round(memory.available / (1024 ** 3), 2),
            "used_percent": memory.percent
        },
        "disk": {
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "free_gb": round(disk.free / (1024 ** 3), 2),
            "used_percent": disk.percent
        }
    }
