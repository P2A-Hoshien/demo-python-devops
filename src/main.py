from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI(title="DevOps Demo API")


@app.get("/health")
def health_check():
    """心跳检查接口"""
    return {"status": "ok"}

@app.get("/info")
def info():
    """返回主机信息和当前时间"""
    hostname = socket.gethostname()
    now = datetime.utcnow().isoformat() + "Z"
    return {"hostname": hostname, "time": now}

