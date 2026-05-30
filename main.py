from fastapi import FastAPI
from routes import system

app = FastAPI(
    title="Linux Command Executor API",
    description="A secure API to execute predefined Linux system commands."
)

# Required Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Standard Routing Include
app.include_router(system.router)