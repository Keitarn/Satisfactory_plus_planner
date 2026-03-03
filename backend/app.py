from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

items: List[Item] = []

@app.get("/api/items")
def get_items():
    return items

@app.post("/api/items")
def add_item(item: Item):
    items.append(item)
    return item