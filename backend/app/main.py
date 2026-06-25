from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.api.routes import router
from backend.app.core.config import settings
from backend.app.dependencies import create_protfolio_assistant_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.portfolio_assistant_service = create_protfolio_assistant_service()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.version,
    lifespan=lifespan,
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
