from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

log = logging.getLogger(__name__)

# here we define the custom handler for HTTPException


async def http_exception_handler(request: Request, exc: HTTPException):
    log.error(f"HTTP {exc.status_code} error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

#here we custom exception for ValueError (For validation or Business Logic Erros)
async def value_error_handler(request: Request, exc: ValueError):
    log.error(f"ValueError occured:{str(exc)}")
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )



#here we custom exception for general exception
async def general_exception_handler(request: Request, exc: Exception):
    log.error(f"An unexpected error occurred: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"},
    )
        