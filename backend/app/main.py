from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(
    title="Leela AI Portfolio",
    description="AI powered portfolio platform",
    version="1.0.0"
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
