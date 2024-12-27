from fastapi import FastAPI
from app.routers import article

app = FastAPI()

app.include_router(article.router)
