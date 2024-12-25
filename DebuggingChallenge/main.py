from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items_db = {}

@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    item_id = len(items_db) + 1  
    items_db[item_id] = item
    return {"id": item_id, "name": item.name, "price": item.price}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = get_item_by_id(item_id)
    return item

def get_item_by_id(item_id: int):
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
