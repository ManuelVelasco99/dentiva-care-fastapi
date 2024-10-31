from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.auth.hashing import verify_password
from src.auth.jwt import create_access_token
from src.db import user_collection
from datetime import datetime, timedelta
from jose import JWTError
import os
from src.auth.jwt import create_access_token, verify_token

router = APIRouter()

# Load environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Define request models
class LoginRequest(BaseModel):
    username: str
    password: str

class CheckTokenRequest(BaseModel):
    token: str

# Login endpoint
@router.post("/login")
async def login_user(login_request: LoginRequest):
    user = await user_collection.find_one({"email": login_request.username})
    if not user or not verify_password(login_request.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": login_request.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Token validation endpoint
@router.post("/validate")
async def check_token(request_body: CheckTokenRequest):
    try:
        # Decode and validate token
        payload = verify_token(request_body.token)
        if payload is None:
            return {"valid": False, "message": "Invalid or expired token"}

        sub = payload.get("sub")
        exp = payload.get("exp")

        # Ensure both 'sub' and 'exp' are present
        if sub and exp:
            # Convert exp timestamp to datetime for comparison
            if datetime.utcnow() > datetime.fromtimestamp(exp):
                return {"valid": False, "message": "Token has expired"}

            return {"valid": True, "uid": sub}
        else:
            return {"valid": False, "message": "Invalid token structure"}

    except JWTError as error:
        print(error)
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="A server error occurred, contact system administrators.")
