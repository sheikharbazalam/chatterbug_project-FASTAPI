
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from app.api.password import router as password_router
from app.api.bitcoin import router as bitcoin_router
from fastapi.middleware.cors import CORSMiddleware
import httpx
import logging
import secrets
import string
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import aioredis
from contextlib import asynccontextmanager


# Create FastAPI instance
app = FastAPI()

# Add a route to fetch the current Bitcoin price
origins = [
    # Vue.js frontend (replace with your actual frontend URL)
    "http://localhost:8080",
    "http://localhost",       # Localhost can also be used during development
    # For example, if using React or Vue or Angular any other frontend on this port
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow these origins to access your backend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# adding logging
logging.basicConfig(level=logging.INFO,   format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])

# Rate limiting


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = await aioredis.from_url("redis://localhost")
    await FastAPILimiter.init(redis)

    yield
    await redis.close()

app = FastAPI(lifespan=lifespan)


class PasswordRequest(BaseModel):
    length: int
    include_uppercase: bool = True
    include_numbers: bool = True
    include_special: bool = True
    include_lowercase: bool = True


@app.post("/generate-password", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def generate_password(request: PasswordRequest):
    length = request.length

    # Enforce minimum password length
    if length < 12:
        raise HTTPException(
            status_code=400, detail="Password length must be at least 12 characters.")

    # Check if at least one type of character is included and build the character set based on the user preferences
    character_set = ""

    if request.include_lowercase:
        character_set += string.ascii_lowercase
    if request.include_uppercase:
        character_set += string.ascii_uppercase

    if request.include_numbers:
        character_set += string.digits
    if request.include_numbers:
        character_set += string.digits

    if request.include_special:
        character_set += "!@#$%^&*()"

    if not character_set:
        logging.error("No character types selected.")
        raise HTTPException(
            status_code=400, detail="At least one type of character must be included.")

    # Generate secure password
    password = ''.join(secrets.choice(character_set) for _ in range(length))
    # Log the generated password for auditing and debugging purposes
    logging.info(f"Generated password successfully: {length}")

    # Return the generated password
    return {"password": password, "length": length}


@ app.get("/bitcoin-price")
async def get_bitcoin_price():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")

        if response.status_code == 200:
            data = response.json()
            bitcoin_price = data.get("bitcoin", {}).get("usd")
            return {"bitcoin_price_usd": bitcoin_price}
        else:
            raise HTTPException(status_code=response.status_code,
                                detail="Error fetching Bitcoin price")

    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500, detail=f"Error connecting to the API: {e}")

# Include routers
app.include_router(password_router)
app.include_router(bitcoin_router)
