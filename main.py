from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from fastapi import FastAPI,Response,status,HTTPException
app=FastAPI()
class post(BaseModel):
    title: str
    content: str
    publish: bool = True 
    rating: Optional[int]=None

my_posts=[{"title":"title of post 1","content":"content of post 1","id": 1},{"title":"favorite foods","content":"i like pizza","id":2}]
# funcyion for finding a post
def find_post(id):
	for p in my_posts:
		if p["id"]==id:
			return p
 
@app.get("/")
def root():
    return {"message": "welcome to my api__"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# helps in validate the data it recives from client
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:post):
	post_dict=post.dict()
	post_dict['id']=randrange(0,10000000)
	my_posts.append(post_dict)
	return {"data":post_dict}

# function for latest post
# @app.get("/posts/latest")
# def get_latest_post():
# 	post= my_posts[len(my_posts)-1]
# 	return {"detail":post}
#retriving one individual post


@app.get("/posts/{id}")
def get_post(id:int,response:Response):
	post=find_post(id)
	if not post:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
		# return {'message':f"post with id:{id} was not found"}
		# response.status_code=status.HTTP_404_NOT_FOUND
	return{"post_detail":post}
