from fastapi import FastAPI, HTTPException
from app.api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
import aioredis
from contextlib import asynccontextmanager
import logging
from app.error_handlers import http_exception_handler, value_error_handler, general_exception_handler


# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)
app = FastAPI()

# Register the custom exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(ValueError, value_error_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Initialize FastAPILimiter
# Initialize Redis for rate limiting


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = await aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis)
    yield
    await redis.close()

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
origins = [
    "http://localhost:8080",  # Frontend origin
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}
