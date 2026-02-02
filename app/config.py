import os
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
class Settings(BaseSettings):
    # Cloudflare R2 settings
    aws_access_key_id: str = None
    aws_secret_access_key: str = None
 

    # Astra DB settings
    astra_db_client_id: str = Field(..., env="ASTRA_DB_CLIENT_ID")
    astra_db_client_secret: str = Field(..., env="ASTRA_DB_CLIENT_SECRET")
    
    class Config:
        env_file = ".env"
        extra = "ignore"  # This will ignore any extra fields in .env

@lru_cache
def get_settings():
    return Settings()