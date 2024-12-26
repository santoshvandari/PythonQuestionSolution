### **1. Swagger and OpenAPI Integration**
FastAPI automatically generates interactive API documentation:
- **Swagger UI**: Available at `/docs` (e.g., `http://127.0.0.1:8000/docs`).
- **ReDoc**: Available at `/redoc` (e.g., `http://127.0.0.1:8000/redoc`).

These are enabled by default and provide a user-friendly way to interact with and test the API.

---

### **2. API Endpoints Documentation**

The following endpoints will now be documented in the Swagger UI:

#### **POST `/posts/`**
- **Description**: Create a new blog post.
- **Request Body**:
  ```json
  {
    "title": "Blog Title",
    "content": "Blog Content",
    "author": "Author Name"
  }
  ```
- **Response**:
  - **201**: The created blog post.
  - **400**: Blog with this title already exists.

#### **GET `/posts/`**
- **Description**: Retrieve all blog posts.
- **Response**:
  - **200**: List of blog posts.

#### **PUT `/posts/{title}`**
- **Description**: Update an existing blog post by title.
- **Path Parameter**:
  - `title`: The title of the blog post to update.
- **Request Body** (optional fields):
  ```json
  {
    "content": "Updated Content",
    "author": "Updated Author"
  }
  ```
- **Response**:
  - **200**: The updated blog post.
  - **404**: Blog not found.

#### **DELETE `/posts/{title}`**
- **Description**: Delete a blog post by title.
- **Path Parameter**:
  - `title`: The title of the blog post to delete.
- **Response**:
  - **204**: Successful deletion.
  - **404**: Blog not found.

---

### **3. Testing the Documentation**

Run the application and navigate to the following URLs:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
  - Provides an interactive interface for testing endpoints.
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
  - Offers a detailed view of the API schema.

---
