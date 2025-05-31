from typing import List, Optional
from src.database import get_db
from models.product import Product

def create_product(product: Product) -> Product:
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, category, stock) VALUES (?, ?, ?, ?)",
            (product.name, product.price, product.category, product.stock)
        )
        conn.commit()
        return product

def get_all_products() -> List[Product]:
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, category, stock FROM products")
        products = cursor.fetchall()
        return [Product(**dict(p)) for p in products]

def get_product_by_id(product_id: int) -> Optional[Product]:
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name, price, category, stock FROM products WHERE id = ?",
            (product_id,)
        )
        row = cursor.fetchone()
        if row:
            return Product(**dict(row))
        return None

def update_product(product_id: int, product: Product) -> bool:
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET name = ?, price = ?, category = ?, stock = ? WHERE id = ?",
            (product.name, product.price, product.category, product.stock, product_id)
        )
        conn.commit()
        return cursor.rowcount > 0

def delete_product(product_id: int) -> bool:
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        return cursor.rowcount > 0