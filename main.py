from fastapi import FastAPI
from src.routes import user
from src.routes import auth

app = FastAPI()

app.include_router(user.router, prefix="/users")
app.include_router(auth.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"message": "API de gestión de dental para el proyecto dentiva-care-fastapi"}
