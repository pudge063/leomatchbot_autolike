import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
phone_number = os.getenv("phone_number")

SAVE_PATH = "all_images"