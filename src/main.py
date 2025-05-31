from fastapi import FastAPI
from api.routes import router as product_router
from src.database import create_tables

app = FastAPI()

# Ensure the database tables are created at startup
create_tables()

# Include the product router
app.include_router(product_router)
