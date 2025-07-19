from fastapi import APIRouter, Query
from app import schemas
from app.db import orders_collection, products_collection
import uuid

router = APIRouter()

@router.post("/orders", response_model=schemas.OrderCreateResponse, status_code=201)
def create_order(order: schemas.OrderCreate):
    generated_id = str(uuid.uuid4().int)[:9]
    doc = {
        "id": generated_id,
        "userId": order.userId,
        "items": [{"productId": item.productId, "qty": item.qty} for item in order.items]
    }
    orders_collection.insert_one(doc)
    return {"id": generated_id}

@router.get("/orders/{user_id}", response_model=schemas.OrderListResponse)
def list_orders(user_id: str, limit: int = Query(0), offset: int = Query(0)):
    cursor = orders_collection.find({"userId": user_id}).skip(offset).limit(limit)
    orders = []
    for doc in cursor:
        items = []
        total = 0.0
        for item in doc["items"]:
            product = products_collection.find_one({"id": item["productId"]})
            if product:
                product_details = {"name": product["name"], "id": product["id"]}
                items.append({"productDetails": product_details, "qty": item["qty"]})
                total += product["price"] * item["qty"]
        orders.append({
            "id": doc["id"],   
            "items": items,
            "total": total
        })

    page_info = {
        "next": offset + limit,
        "limit": limit,
        "previous": offset - limit
    }

    return {"data": orders, "page": page_info}