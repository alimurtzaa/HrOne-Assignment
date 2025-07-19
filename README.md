# HROne Backend Task (E-commerce APIs)

This project is a sample **backend application** built with FastAPI & MongoDB for an e-commerce use case.  
It was built as part of the **HROne Backend Intern Hiring Task**.

---

## 🚀 **Tech Stack**
- Python 3.10+
- FastAPI
- pymongo (MongoDB driver)
- MongoDB Atlas (free M0 cluster)
- Uvicorn (server)
- Python dotenv (for environment variables)

 
---

## 📌 **APIs Implemented**

### ✅ Create Product
- `POST /products`
- Request body:
```json
{
  "name": "Sample Product",
  "price": 100.0,
  "sizes": [
    {"size": "large", "quantity": 10}
  ]
}
```
- Response body:
```json
{ "id": "123456789" }
```

### ✅ List Products

- `GET /products`
- Query params: name, size, limit, offset
- Response body:
```json
{
  "data": [
    {"id": "12345", "name": "Sample", "price": 100.0},
    ...
  ],
  "page": { "next": 10, "limit": 10, "previous": 0 }
}

```
### ✅ Create Order
- `POST /orders`
- Request body:
```json
{
  "userId": "user_1",
  "items": [
    {"productId": "123456789", "qty": 3},
    {"productId": "222222222", "qty": 2}
  ]
}

```
- Response body:
```json
{ "id": "987654321" }
```

### ✅ List Orders

- `GET /products/{user_id`
- Query params: limit, offset
- Response body:
```json
{
  "data": [
    {
      "id": "order123",
      "items": [
        {
          "productDetails": { "name": "Sample Product", "id": "123456" },
          "qty": 3
        }
      ],
      "total": 300.0
    }
  ],
  "page": { "next": 10, "limit": 10, "previous": 0 }
}
```

---

## ☁ Deployment
Deploy on Railway (free tier)

---

## ✨ Author
Murtza Ali
