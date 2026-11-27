from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PRODUCTS = [
    {"id": 1, "name": "Механическая клавиатура", "price": 8500},
    {"id": 2, "name": "Беспроводная мышь", "price": 4200},
    {"id": 3, "name": "Монитор 27 дюймов", "price": 24000},
    {"id": 4, "name": "Наушники с шумоподавлением", "price": 12900},
]

class Order(BaseModel):
    items: list[int]

@app.get("/api/products")
def get_products():
    return PRODUCTS

@app.post("/api/order")
def create_order(order: Order):
    if not order.items:
        raise HTTPException(status_code=400, detail="Корзина пуста")
    total = sum(p["price"] for p in PRODUCTS if p["id"] in order.items)
    return {"status": "ok", "message": f"Заказ оформлен! Сумма к оплате: {total} ₽"}
