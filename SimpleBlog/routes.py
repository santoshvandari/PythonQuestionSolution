from fastapi import APIRouter, HTTPException
from typing import List
from app.models.post import Post, PostUpdate

router = APIRouter()

# In-memory storage for posts (a dictionary using titles as keys)
posts_db = {}

@router.post("/posts/", response_model=Post, status_code=201)
def create_post(post: Post):
    if post.title in posts_db:
        raise HTTPException(status_code=400, detail="Post with this title already exists.")
    posts_db[post.title] = post
    return post

@router.get("/posts/", response_model=List[Post])
def get_posts():
    return list(posts_db.values())

@router.put("/posts/{title}", response_model=Post)
def update_post(title: str, post_update: PostUpdate):
    if title not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found.")
    
    current_post = posts_db[title]
    if post_update.content:
        current_post.content = post_update.content
    if post_update.author:
        current_post.author = post_update.author
    
    posts_db[title] = current_post
    return current_post

@router.delete("/posts/{title}", status_code=204)
def delete_post(title: str):
    if title not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found.")
    
    del posts_db[title]
    return None
