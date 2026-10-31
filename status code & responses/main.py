from fastapi import FastAPI,HTTPException
from starlette.status import HTTP_201_CREATED

app=FastAPI()

@app.post("/create_user",status_code=HTTP_201_CREATED)
def create_user():
    
    return{
        "message":"user created!"
    }

@app.get("/user")
def get_users():
    return {
        "status":"success",
        "message":"user fetched",
        "data":{
            "name":"mohit",
            "age":24
        }
    }
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(status_code=404,detail="User not Found")
    return {
        "id":1,
        "name":"ishant"
    }
