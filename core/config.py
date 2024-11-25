import os

class Config:
    DATABASE_DEVELOPMENT = os.getenv("DATABASE_DEVELOPMENT")
    
settings = Config()