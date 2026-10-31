from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

@app.exception_handler(Exception)
async def global_exception_handler(request : Request , exc : Exception):

    logger.exception("unexpected Error Occured",request.method,request.url.path)

    return JSONResponse(
        status_code=500,
        content={
            "Error":"Internal Server Error",
            "message":"Something went Wrong"
        }
    )

@app.get("/user/{user_id}")
def get_user(user_id : int):
    if user_id == 999:
        raise HTTPException(         #use this if you are expecting the error
            status_code=404,
            detail = "User not found"
        )
    if user_id==500:
        result = 10/0  #This is unexcpected error which will go to the Global exception handler

    return {"id":user_id,"name":"Ishant"}