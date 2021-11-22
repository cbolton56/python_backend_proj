from typing import Optional
from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    published: bool = True
    rating: Optional[int]  = None

@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/") 
def get_post(): 
    return {"data":"This is your posts"}

@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.title)
    print(new_post.content)
    return {"data": new_post} 
    
