from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="AI Search Engine",
    version="0.2.0",
    description="Production AI Search Engine Backend"
)

app.include_router(router)