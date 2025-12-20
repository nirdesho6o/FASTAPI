from fastapi import FastAPI,Body
from pydantic import BaseModel
from typing import Optional


app=FastAPI()
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}


my_posts = [{"title": "First Post", "content": "This is my first post"},
            {"title": "Second Post", "content": "This is my second post"}]


@app.get("/posts")
def get_posts():
    return {"data": my_posts}

#pydantic model 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.post("/posts")
def create_posts(new_post: Post):
    print (new_post)
    #to convert pydantic model to dictionary
    print(new_post.model_dump())
    return{"data":new_post}