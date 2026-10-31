from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

app=FastAPI()

@app.exception_handler(Exception)
def global_handler_exception(request:Request , exc: Exception):
    logger.exception("Unexpected Error Occured") #shows in server logs along with traceback
    return JSONResponse(
        status_code=500,
        content={
            "error":"Internal Server Error",
            "message":"something went wrong"
        }
    )



@app.get("/divide")
def divide():
    
    result = 10/0
    return {
        "Result":result
    }
    
