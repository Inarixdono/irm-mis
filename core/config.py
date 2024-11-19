from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DATABASE_URI = os.getenv("DATABASE_URI")
    
settings = Config()