from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from app.services.password_services import check_password_strength, generate_password
from fastapi.responses import JSONResponse


router = APIRouter()


class PasswordRequest(BaseModel):
    length: int = Field(..., ge=12, le=128,
                        description="Password length between 12 and 128 characters")
    include_special: bool = False
    include_numbers: bool = True


def get_password_generator():
    return generate_password

# Endpoint to generate password


@router.post("/generate-password")
async def generate_password_route(req: PasswordRequest, generate_password=Depends(get_password_generator)):
    if req.length < 12 or req.length > 128:
        raise HTTPException(
            status_code=400, detail="Password length must be at least 12 characters.")
    if not (req.include_special or req.include_numbers):
        raise HTTPException(
            status_code=400, detail="At least one character type must be included.")

    try:
        password = generate_password(
            req.length, req.include_special, req.include_numbers)
        strength = check_password_strength(password)
        return {"password": password, "strength": strength}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred")


# Endpoint to check password strength
@router.post("/check-password-strength")
def check_password_strength_route(password: str):
    strength = check_password_strength(password)
    return {"password": password,  "strength": strength}
