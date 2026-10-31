
from fastapi import FastAPI,Request
import time
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def middleware_loggin(request : Request , call_next):

    start_time = time.time()   

    response = await call_next(request)

    process_time=time.time()-start_time

    logger.info(
        "%s %s → %s (%.4f seconds)",
        request.method,
        request.url.path,
        response.status_code,
        process_time
    )

    return response

@app.get("/hello")
def hello():
    return {
        "message" :"hello"
    }



