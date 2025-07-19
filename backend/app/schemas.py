from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

# product related schemas
class SizeItem(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeItem]

class ProductCreateResponse(BaseModel):
    id: str

class ProductListItem(BaseModel):
    id: str
    name: str
    price: float

class PageInfo(BaseModel):
    next: int
    limit: int
    previous: int

class ProductListResponse(BaseModel):
    data: List[ProductListItem]
    page: PageInfo

class OrderCreate(BaseModel):
    user_id: str
    product_ids: List[str]

class Order(OrderCreate):
    id: str
    order_date: datetime

# order related schemas
class OrderItemCreate(BaseModel):
    productId: str  
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItemCreate]

class OrderCreateResponse(BaseModel):
    id: str

class OrderItemResponse(BaseModel):
    productDetails: dict  
    qty: int

class OrderListItem(BaseModel):
    id: str
    items: List[OrderItemResponse]
    total: float

class OrderListResponse(BaseModel):
    data: List[OrderListItem]
    page: PageInfo