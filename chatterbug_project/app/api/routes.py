from fastapi import APIRouter
from app.api import bitcoin, password

router = APIRouter()

router.include_router(bitcoin.router)
router.include_router(password.router)
