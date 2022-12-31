from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

#makes the root function into a endpoint for the API
#This decorator refrences the path in this case 
#the path is url/ if we change the str to /login the user has to go
#to url/login

#.get is the use of the GET http request
@app.get("/")

# Async is used when we do a asynchronous task
async def root():
    return {'message':'welcome to my new api!!!'}

@app.get('/posts')
def get_posts():
    return {"data":"This is you post"}

@app.post("/post")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {'message':'succesfully created posts'}


#Now this will show message hello world on the website
