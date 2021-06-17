# Standard Library
from functools import lru_cache

# Third Party
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = "dev"

    @staticmethod
    @lru_cache
    def get():
        return Settings()
