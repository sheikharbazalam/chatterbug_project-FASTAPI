from fastapi import FastAPI, HTTPException
from app.api.password import router as password_router
from app.api.bitcoin import router as bitcoin_router
from fastapi.middleware.cors import CORSMiddleware
import httpx
import logging

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


#adding logging
logging.basicConfig(level=logging.INFO,   format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.FileHandler, logging.StreamHandler])



@app.get("/bitcoin-price")
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