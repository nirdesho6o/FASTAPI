from fastapi import FastAPI,Body,Response,status,HTTPException
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

#IMPORTANT -this is writtten before posts/{id} so that it does not conflict with it
@app.get("/posts/latest")   #to get the latest post
def get_latest_post():
    latest_post = my_posts[-1]
    return {"latest_post": latest_post}


@app.get("/posts/{id}")    #to get a specific post by id
def get_post(id: int,response: Response):  #path parameter is int type
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Post not found"}
    return {"post_detail": post}

#not the best way , but works for now
def find_post(id):   #helper function to find a post by id
    for post in my_posts:
        if post['id'] == id:
            return post