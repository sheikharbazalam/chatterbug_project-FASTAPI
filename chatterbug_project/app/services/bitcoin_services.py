import httpx
from fastapi import HTTPException
import logging


async def get_bitcoin_price():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")

        if response.status_code == 200:
            data = response.json()
            bitcoin_price = data.get("bitcoin", {}).get("usd")
            return bitcoin_price
        else:
            raise HTTPException(status_code=response.status_code,
                                detail="Error fetching Bitcoin price")
    except httpx.RequestError as e:
        logging.error(f"Error connecting to the API: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error connecting to the API: {e}")
