from fastapi import FastAPI
from backend.app.api.routes import router
from backend.app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.version
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
