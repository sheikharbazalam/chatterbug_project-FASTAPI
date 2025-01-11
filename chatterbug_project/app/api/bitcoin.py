from fastapi import APIRouter, HTTPException
import httpx
import os

from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

BITCOIN_API_URL = os.getenv("BITCOIN_API_KEY")


<<<<<<< Tabnine <<<<<<<
@router.get("/bitcoin-price")
async def get_bitcoin_price():
    """#+
    Fetch the current Bitcoin price in USD from a third-party API.#+
#+
    This function makes an asynchronous HTTP GET request to the specified API URL,#+
    which is expected to return a JSON response containing the current Bitcoin price.#+
    If the request is successful (status code 200), the function extracts the Bitcoin#+
    price from the response and returns it as a dictionary. If the request fails or#+
    encounters an error, it raises an HTTPException with an appropriate error message.#+
#+
    Parameters:#+
    None#+
#+
    Returns:#+
    dict: A dictionary containing the current Bitcoin price in USD. The dictionary has the#+
    following structure: {"bitcoin_price_usd": <float>}#+
    """#+
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
>>>>>>> Tabnine >>>>>>># {"conversationId":"900db70b-f5e3-4e7e-a7f8-e1d9ba5df165","source":"instruct"}
