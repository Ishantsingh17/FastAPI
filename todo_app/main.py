from typing import Any


from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/create")                    
def create_todo(todo: Todo):
    todos.append(todo)
    return{"message":"todo added", "data":todo}

@app.get("/read_details")
def read_todos():
    return todos


@app.get("/read/{id}")
def get_todo(id : int):
    for i in todos:
        if(i.id==id):
            return i
    
    return {"message":"Todo Not Found !"}

@app.put("/update_todo/{id}")
def update_todo(id:int , updated_todo:Todo):
    for i,todo in enumerate(todos):
        if(todo.id==id):
            todos[i]=updated_todo
            return{
            "message":"todo updated",
            "data":updated_todo
            }
    return {"error":"Todo Not Found"}

@app.delete("/delete_todo/{id}")
def deleted_todo(id:int):
    for i in todos:
        if(i.id==id):
            todos.remove(i)
            return {"message":"Todo Item deleted"}
    
    return {"error":"Todo Not Found"}