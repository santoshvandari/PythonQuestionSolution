# Backend Developer (Python) Assignment

## Instructions

You can attempt as many questions as you like; there’s no limit to how many you can solve.

Using AI to assist with understanding and answering questions is encouraged. However, assignments consisting solely of AI-generated content, without incorporating your own creative and critical thinking, will not be accepted.

---

## Questions

### 1. Development
Create a FastAPI-based application for managing a simple blog with the following functionalities:

- **Create a new post** (title, content, and author).
- **Retrieve a list of all posts**.
- **Update an existing post by title**.
- **Delete a post by title**.

The posts should be stored in memory (you can use an in-memory Python list or dictionary for simplicity). Make sure to:

- Use Pydantic models to validate data.
- Structure the project with appropriate directories (e.g., `models`, `routes`, `main app`).

### 2. API Documentation
Building on top of the first task, generate an API documentation using FastAPI’s built-in features, such as Swagger and OpenAPI. Make sure the API is well-documented, including descriptions, parameter validation, response models, and possible error responses.

### 3. Debugging Challenge
Here is a sample FastAPI app with intentional errors. Your task is to debug the code, fix the issues, and ensure it works as expected. Fix the missing implementation (`get_item_by_id`) and correct any issues related to error handling or validation. Write a brief explanation of the changes you made.

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

### 4. Refactoring Challenge
The following code snippet includes redundant logic. Refactor it to improve readability, maintainability, and avoid duplication. Extract common validation logic into separate utility functions, and refactor the code to be DRY (Don't Repeat Yourself). Also, explain why this is an improvement.

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/")
async def create_user(name: str, email: str, password: str):
    if len(password) < 8:
        raise ValueError("Password too short")
    if "@" not in email:
        raise ValueError("Invalid email")
    return {"name": name, "email": email}

@app.put("/users/")
async def update_user(name: str, email: str, password: str):
    if len(password) < 8:
        raise ValueError("Password too short")
    if "@" not in email:
        raise ValueError("Invalid email")
    return {"name": name, "email": email}
```

### 5. NoSQL Challenge
You are given the following MongoDB collections for an online store:

- **products** (`product_id`, `name`, `category`, `price`, `stock_quantity`)
- **orders** (`order_id`, `user_id`, `product_ids`, `order_date`, `total_amount`)
- **users** (`user_id`, `name`, `email`, `address`)

Write the following MongoDB queries for the store:

1. Find all products in the "Electronics" category that have more than 50 items in stock.
2. Find the total number of orders placed by a user (given their `user_id`), including the total amount spent.
3. List all users who have purchased a specific product (given its `product_id`), including their name and email address.
4. Update the stock quantity of a product (given its `product_id`) after an order is placed, considering the quantity of the product purchased in the order.

### 6. Unit Test Challenge
Below is a sample pseudocode that calculates the perimeter of a rectangle by taking the length and breadth as input. Create a Pytest (snippet will be enough) to ensure maximum test coverage, such that every line inside the function body is executed at least once.

```python
function perimeter(length, breadth) {
    if(!length || !breadth) {
        throw Exception(‘Undefined’);
    }
    
    if(length is not Number) {
        throw Exception(‘Not a number’);
    }
    
    if(breadth is not Number) {
        throw Exception(‘Not a number’);
    }
                   
    if(length < 0 OR breadth < 0) {
        throw Exception(‘dimension cannot be negative’);
    }
   
    return 2 * (length + breadth);
}
```

### 7. Bonus
Integrate MinIO with a FastAPI application to handle file uploads. The app should:

- Allow users to upload a file (e.g., a .txt or .pdf file).
- Store the uploaded files in a MinIO bucket.
- Provide an endpoint to retrieve the uploaded file from MinIO using its URL.

---

## Submission Instructions

### Code-Related Assignments:
Push your code to an online Git hosting platform like GitHub as a public repository and share the repository link by replying to the same email. Also, please document the steps to run your code locally.

### Non-Code Assignments:
Upload your materials (e.g., files, sheets, etc.) to a cloud storage service like Google Drive or OneDrive. Share the publicly accessible link in your reply to the same email.

Alternatively, you can attach the files directly in your reply to the email.

---

**All the best!**

&copy; Darse Technologies, 2024
