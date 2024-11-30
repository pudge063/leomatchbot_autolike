import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
like_count = int(os.getenv("LIKE_COUNT"))
