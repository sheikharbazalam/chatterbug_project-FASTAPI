import os
from dotenv import load_dotenv

load_dotenv()

BITCOIN_API_URL = os.getenv('BITCOIN_API_KEY')
