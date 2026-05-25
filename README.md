# Assignment-Basic-Linux-Command

A secure FastAPI application that executes predefined Linux system commands and returns outputs in JSON format.

## Features
- Secure execution using Python `subprocess` (No raw shell injection allowed)
- Structured API layout
- Automatic interactive documentation via Swagger UI

## API Endpoints
- `GET /health` - Application health status
- `GET /system/uptime` - System uptime info
- `GET /system/disk` - Disk space usage (`df -h`)
- `GET /system/memory` - Memory stats (`free -m`)
- `GET /system/user` - Current active user (`whoami`)

## Setup & Run Instructions
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Start server: `uvicorn main:app --reload`
