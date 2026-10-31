import sqlite3
from fastapi import FastAPI

app = FastAPI()

connection = sqlite3.connect("user.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

connection.commit()

@app.get("/")
def hello():
    return {"message":"sqlite connected"}