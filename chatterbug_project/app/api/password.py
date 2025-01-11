from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils import generate_password

router = APIRouter()

# Define the input schema for the POST request


class PasswordRequest(BaseModel):
    length: int
    include_special: bool = False
    include_numbers: bool = True

# Password generation endpoint


@router.post("/generate-password")
async def generate_password_route(req: PasswordRequest):
    try:
        # Generate the password using the utility function
        password = generate_password(
            req.length, req.include_special, req.include_numbers)
        return {"password": password, "length": len(password)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
