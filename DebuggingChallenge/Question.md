# Debugging Challenge

Here is a sample FastAPI app with intentional errors. Your task is to debug the code, fix the issues, and ensure it works as expected. Fix the missing implementation `(get_item_by_id)` and correct any issues related to error handling or validation. Write a brief explanation of the changes you made.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise ValueError("Price cannot be negative")
    return {"name": item.name, "price": item.price}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = get_item_by_id(item_id)
    return item
```