# Blog API with FastAPI

This is a simple blog API built using FastAPI, allowing you to manage blog posts with functionalities to create, read, update, and delete posts.

## Features

- Create a new blog post (title, content, and author).
- Retrieve a list of all blog posts.
- Update an existing blog post by title.
- Delete a blog post by title.

## Prerequisites

- Python
- pip 

## Installation and Setup

1. **Clone the Repository**  

2. **Create a Virtual Environment**  
   It is recommended to use a virtual environment for the project:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Install the required dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   Start the FastAPI development server:
   ```bash
    fastapi dev main.py
   ```

5. **Access the API**  
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints
- **GET /posts/**: Retrieve all blog posts.
- **POST /posts/**: Create a new blog post.
- **PUT /posts/{title}/**: Update an existing blog post.
- **DELETE /posts/{title}/**: Delete a blog post.