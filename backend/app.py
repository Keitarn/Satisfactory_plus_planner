from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from typing import List, Dict
import json

app = FastAPI()

# Liste globale
items: List[Dict] = []

# Chemin du fichier JSON
filepath = Path("recipes.json")

# Charger le JSON au démarrage
def load_items():
    global items
    if not filepath.exists():
        print("JSON de recette non trouvé, création d'un fichier vide")
        items = []
        save_items()  # crée un fichier vide
        return

    # Version qui fonctionne partout
    with open(filepath, "r", encoding="utf-8") as f:
        items = json.load(f)

# Sauvegarder le JSON
def save_items():
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

load_items()

@app.get("/api/items")
def get_items():
    return items

@app.post("/api/items")
async def add_item(request: Request):
    try:
        item = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="JSON invalide")

    if any(existing.get("code") == item.get("code") for existing in items):
        raise HTTPException(status_code=400, detail="Item avec ce code existe déjà")

    items.append(item)
    save_items()
    return item

@app.put("/api/items/{code}")
async def update_item(code: str, request: Request):
    try:
        new_data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="JSON invalide")

    for idx, existing in enumerate(items):
        if existing.get("code") == code:
            items[idx] = new_data
            save_items()
            return new_data

    raise HTTPException(status_code=404, detail="Item non trouvé")