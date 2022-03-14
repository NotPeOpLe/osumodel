from typing import List, Optional
from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    api_key: Optional[str] = None
    client_id: Optional[int] = None
    client_secret: Optional[str] = None
    client_redirect_url: Optional[HttpUrl] = None

    class Config:
        env_prefix = 'APIMODEL_'

settings = Settings()
