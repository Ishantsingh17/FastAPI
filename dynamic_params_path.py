'''below code is a simple example of a dynamic path parameter , 
 which is used to get the user id and return the user details
 what is dynamic path parameter?
 Dynamic Path Parameters are parts of a URL that can change dynamically and whose values are passed to your FastAPI function.'''

from fastapi import FastAPI

app = FastAPI()

users = {
    1: {
        "name": "Ishant",
        "age": 21,
        "city": "Pune"
    },
    2: {
        "name": "Varun",
        "age": 22,
        "city": "Delhi"
    },
    3: {
        "name": "Rahul",
        "age": 25,
        "city": "Mumbai"
    }
}


@app.get("/")
def home():
    return {"message": "Welcome to the Users API"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id)