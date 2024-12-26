from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str
    author: str

class BlogUpdate(BaseModel):
    content: Optional[str] = None
    author: Optional[str] = None

    