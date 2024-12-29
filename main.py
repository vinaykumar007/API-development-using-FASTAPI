from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app=FastAPI()
class post(BaseModel):
    title: str
    content: str
    publish: bool = True 
    rating: Optional[int]=None

my_posts=[{"title":"title of post 1","content":"content of post 1","id": 1},{"title":"favorite foods","content":"i like pizza","id":2}]
# async  # async keyword is needed when doing asyncrous tasks remove it 
@app.get("/")# decorate helps in chaging behavior of function as logging get request decortor
def root():
     
    return {"message": "welcome to my api__"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/createposts")
def create_posts(post: post):
    print(post)
    print(post.dict())
    return {"data": "post"}
# title str,content str