import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    if not GOOGLE_API_KEY:
        # Fallback for testing if env var not set, though in prod it should be.
        # Ideally we'd raise an error or warn.
        print("Warning: GOOGLE_API_KEY not found in environment variables.")

config = Config()
