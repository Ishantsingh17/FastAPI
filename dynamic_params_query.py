import string
from fastapi import FastAPI
app= FastAPI()

@app.get("/products")
def get_products(name: str=None,price: int =0):
    return {"name": name, "price":price}