from fastapi import FastAPI
from api.routes import router
from db.connection import initialize_database

initialize_database()

app = FastAPI(title="Number Guessing Game API")
app.include_router(router)
