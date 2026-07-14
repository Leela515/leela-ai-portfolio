from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
