from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from app.utils import generate_password
import logging

router = APIRouter()

# Define the input schema for the POST request

# configure Logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


class PasswordRequest(BaseModel):
    length: int = Field(..., ge=12, le=128,
                        description="password length between 12 to 128 characters")
    include_special: bool = False
    include_numbers: bool = True


class PasswordGeneration(Exception):
    pass


def get_password_generator():
    return generate_password

# Password generation endpoint

# 
@router.post("/generate-password",
             response_description="Generate a secure password",
             responses={
                 200: {"description": "Passsword generated successfully"},
                 400: {"description": "Invalid input parameteres"},
                 # For unexpected errors in the server implementation.
                 500: {"description": "Internal Server Error"}
             },
             )


async def generate_password_route(req: PasswordRequest, generate_password=Depends(get_password_generator)):
    try:
        # Generate the password using the utility function
        password = generate_password(
            req.length, req.include_special, req.include_numbers)
        log.info("Generated password successfully")
        return {"password": password, "length": len(password)}
    except PasswordGeneration as e:
        log.error("Error generating password: {e}")
        
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        log.error(f"Internal error: {e}")
        raise HTTPException(
            status_code=400, detail="An unexpected error occurred")
