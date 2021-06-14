from functools import lru_cache
from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///db.sqlite3"
    APP_NAME: str = 'Table Service'
    REGISTRATION_TOKEN_LIFETIME: int = 60 * 60
    TOKEN_ALGORITHM: str = 'HS256'
    MAIL_SENDER: str = 'noreply@example.com'
    API_PREFIX: str = '/api'
    HOST: str = 'localhost'
    PORT: int = 8000
    BASE_URL: str = f'{HOST}:{str(PORT)}/'
    MODELS:List[str] = [
        #'app.models.table',
        #'app.models.order',
        'app.models.product',
    ]

    class Config:
        case_sensitive: bool = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()