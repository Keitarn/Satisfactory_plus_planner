from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

# Données de test
items: List[Item] = [
    Item(id=1, name="Clavier"),
    Item(id=2, name="Souris"),
    Item(id=3, name="Ecran")
]

@app.get("/api/items")
def get_items():
    return items

@app.post("/api/items")
def add_item(item: Item):
    items.append(item)
    return item