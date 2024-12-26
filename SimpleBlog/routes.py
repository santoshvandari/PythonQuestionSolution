from fastapi import APIRouter, HTTPException
from model import Blog,BlogUpdate

router = APIRouter()

blog_db = {}

@router.post("/posts/")
def create_post(blog: Blog):
    if blog.title in blog_db:
        raise HTTPException(status_code=400, detail="Blog with this title already exists.")
    blog_db[blog.title] = blog
    return {"message": "Blog created successfully.", "data": blog}

@router.get("/posts/")
def get_posts():
    return blog_db

@router.put("/posts/{title}",)
def update_post(title: str, blog_update: BlogUpdate):
    if title not in blog_db:
        raise HTTPException(status_code=404, detail="Blog not found.")
    
    current_post = blog_db[title]
    if blog_update.content:
        current_post.content = blog_update.content
    if blog_update.author:
        current_post.author = blog_update.author
    
    blog_db[title] = current_post
    return {
        "message": "Blog updated successfully.",
        "data": current_post
    }

@router.delete("/posts/{title}")
def delete_post(title: str):
    if title not in blog_db:
        raise HTTPException(status_code=404, detail="Blog not found.")
    
    del blog_db[title]
    return {"message": "Blog deleted successfully.", "data": title}
