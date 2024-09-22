from fastapi import FastAPI
from src.routes import user

app = FastAPI()

# Incluir las rutas
app.include_router(user.router, prefix="/users")

@app.get("/")
def read_root():
    return {"message": "API de gestión de dental para el proyecto dentiva-care-fastapi"}
