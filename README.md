# Tienda API FastAPI

API REST para gestionar productos de una tienda online.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn src.main:app --reload
```

## Endpoints principales

- `GET /` — Bienvenida
- `POST /products` — Crear producto
- `GET /products` — Listar productos
- `GET /products/{id}` — Obtener producto por ID
- `PUT /products/{id}` — Actualizar producto
- `DELETE /products/{id}` — Eliminar producto

Visita `/docs` para la documentación interactiva.