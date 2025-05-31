# Tienda API con FastAPI
API REST para gestionar un catálogo de productos con operaciones CRUD.

## Instalación
1. Clona el repositorio: `git clone <URL>`
2. Crea un entorno virtual: `python -m venv venv`
3. Instala dependencias: `pip install -r requirements.txt`
4. Ejecuta la API: `uvicorn src.main:app --reload`

## Endpoints
- `POST /products`: Crear un producto.
- `GET /products`: Listar todos los productos.
- Ver más en `/docs` (Swagger).

## Tecnologías
- Python, FastAPI, SQLite, Pydantic
- Pruebas: pytest
- Desplegada en: [enlace a Render]

## Ejemplo
```bash
curl -X POST "http://localhost:8000/products" -H "Content-Type: application/json" -d '{"name":"Laptop","price":999.99,"category":"Electronics","stock":10}'
