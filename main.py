from fastapi import FastAPI
from user_routes import router

app = FastAPI()

app.include_router(router)