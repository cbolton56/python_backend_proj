from typing import Optional
from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
import uuid 

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    published: bool = True
    rating: Optional[int]  = None

# To store posts in memory
# Each post is a dict object
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": "1"}, {"title": "title of post 2", "content":"i'm hungry", "id":"2"}]

@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/posts") 
def get_posts(): 
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id):
    p = None
    for post in my_posts: 
        if post["id"] == id: 
            p = post
    if p:
        return {"post": p} 
    else: 
        return "No post found with given ID."

@app.post("/posts")
def create_posts(new_post: Post):
    new_id = str(uuid.uuid4())
    post_dict = new_post.dict()
    post_dict["id"] = new_id
    my_posts.append(post_dict)
    return {"data": new_post} 


