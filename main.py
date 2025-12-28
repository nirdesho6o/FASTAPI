from fastapi import FastAPI,Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}


my_posts = [{"title": "First Post", "content": "This is my first post",'id':1},
            {"title": "Second Post", "content": "This is my second post",'id':2}]


@app.get("/posts")
def get_posts():     #to get all posts
    return {"data": my_posts}

#pydantic model 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True #default value
    rating: Optional[int] = None  #optional field


@app.post("/posts")
def create_posts(new_post: Post):
    print (new_post)
    #to convert pydantic model to dictionary
    print(new_post.model_dump())
    post_dict = new_post.model_dump()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data":post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    for post in my_posts:
        if post['id'] == id:
            return {"post_detail": post}
    return {"message": "Post not found"}