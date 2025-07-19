# app/routers/products.py
from fastapi import APIRouter, Query
from typing import Optional
from app.db import products_collection
from app import schemas
import uuid

router = APIRouter()

@router.post("/products", response_model=schemas.ProductCreateResponse, status_code=201)
def create_product(product: schemas.ProductCreate):
    generated_id = str(uuid.uuid4().int)[:9]  
    doc = product.model_dump()
    doc["id"] = generated_id
    products_collection.insert_one(doc)
    return {"id": generated_id}

@router.get("/products", response_model=schemas.ProductListResponse)
def list_products(
    name: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(0)
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = products_collection.find(query).skip(offset).limit(limit)
    products = []
    for doc in cursor:
        products.append({
            "id": doc["id"],   
            "name": doc["name"],
            "price": doc["price"]
        })

    page_info = {
        "next": offset + limit,
        "limit": limit,
        "previous": offset - limit
    }

    return {"data": products, "page": page_info}


    