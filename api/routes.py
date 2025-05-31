from fastapi import APIRouter, HTTPException
from typing import List
from models.product import Product
from crud.crud import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
)

router = APIRouter()

@router.post("/products", response_model=Product)
def create(product: Product):
    return create_product(product)

@router.get("/products", response_model=List[Product])
def read_all():
    return get_all_products()

@router.get("/products/{product_id}", response_model=Product)
def read_one(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=Product)
def update(product_id: int, product: Product):
    updated = update_product(product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{product_id}")
def delete(product_id: int):
    deleted = delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}