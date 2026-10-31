from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
import logging

from starlette import status


app = FastAPI()
logger = logging.getLogger(__name__)

class UserNotFoundException(Exception):
    pass

@app.exception_handler(UserNotFoundException)
def get_user_not_found_handler(request : Request , exc :UserNotFoundException):

    logger.exception("User not found: %s %s",
        request.method ,
        request.url.path
    )

    return JSONResponse(
        status_code = 404,
        content = {
            "Error":"User not found",
            "message":"User does not exist"
        }
    )

@app.exception_handler(Exception)
def get_global_handler(request:Request , exc : Exception):

    logger.exception("Unexpected Server Error Occured %s %s", request.method , request.url.path)

    return JSONResponse(
        status_code=500,
        content={
            "error":"Internal Server Error",
            "message":"Something went wrong"
        }
    )


@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id==999:
        raise UserNotFoundException()
    
    if user_id==500:
        result = 10/0

    return {
        "id":user_id,
        "name":"Ishant"
    }