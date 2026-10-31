from fastapi import FastAPI,Request,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse


app = FastAPI()

class UserNotFoundException(Exception):
    pass
@app.exception_handler(UserNotFoundException)
def get_user_not_found_handler(request:Request , exc = UserNotFoundException):

    return JSONResponse(
        status_code=404,
        content={
            "error":"user not found",
            "message":"user does not Exist"
        }
    )

@app.exception_handler(Exception)
def get_global_handler(request:Request, exc = Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error":"Internal Server Error",
            "message":"something is wrong"
        }
    )

oAuth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    if(form_data.username!="ishant" and form_data.password!="hero"):
        raise UserNotFoundException()
    
    return {
        "access_token":"abc123",
        "token_type":"bearer"
    }

def get_current_user(token:str = Depends(oAuth2_scheme)):

    if token!="abc123":
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    return{
        "username":"ishant"
    }

@app.get("/profile")
def get_profile(user = Depends(get_current_user)):
    return{
        "message":f"Welcome {user['username']}",
        "user":user
    }


