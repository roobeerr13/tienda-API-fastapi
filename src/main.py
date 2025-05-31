from fastapi import FastAPI
from api.routes import router as product_router
from src.database import create_tables

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de productos de la tienda"}

create_tables()
app.include_router(product_router)