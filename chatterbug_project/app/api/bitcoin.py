from fastapi import APIRouter, HTTPException
import httpx
import os

from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

BITCOIN_API_URL = os.getenv("BITCOIN_API_KEY")


@router.get("/bitcoin-price")
async def get_bitcoin_price():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BITCOIN_API_URL)

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
