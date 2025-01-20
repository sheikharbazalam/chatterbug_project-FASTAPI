from fastapi import APIRouter, HTTPException
from app.services.bitcoin_services import get_bitcoin_price

router = APIRouter()


@router.get("/bitcoin-price")
async def bitcoin_price():
    price = await get_bitcoin_price()
    return {"bitcoin_price_usd": price}
