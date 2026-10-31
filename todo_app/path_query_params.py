
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


todos = [
    {
        "id": 1,
        "user_id": 101,
        "title": "Learn FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "user_id": 101,
        "title": "Learn Python",
        "completed": True
    },
    {
        "id": 3,
        "user_id": 102,
        "title": "Learn Pydantic",
        "completed": False
    }
]


@app.get("/users/{user_id}/todos")
def get_todos(
    user_id: int,
    completed: bool = None,
    limit: int = 10
):

    # First: Find todos for this particular user
    user_todos = []

    for todo in todos:
        if todo["user_id"] == user_id:
            user_todos.append(todo)

    # Second: Filter by completed status if provided
    if completed is not None:
        filtered_todos = []

        for todo in user_todos:
            if todo["completed"] == completed:
                filtered_todos.append(todo)

        user_todos = filtered_todos

    # Third: Limit the number of results
    return user_todos[:limit]
    
