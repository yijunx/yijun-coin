# -------------------------------------------------------------------------------------------------------------
# Copyright (c) UCARE.AI Pte Ltd. All rights reserved.
# -------------------------------------------------------------------------------------------------------------
import os
from enum import Enum

from pydantic import BaseSettings


class Settings(BaseSettings):
    # basics
    ENV: str = "local-dev"
    SERVICE_NAME: str = "yijun-coin"
    SERVICE_VERSION: str = "local-ver"

    DATABASE_URI: str


class ProductionConfig(Settings):
    # it means that, every entry for Settings must
    # come from environment variables
    pass


class DevelopmentConfig(Settings):
    class Config:
        env_file = "./config/dev.env"


def find_which_config():
    if os.getenv("ENV"):  # there is DOMAIN name provided
        config = ProductionConfig()
    else:
        config = DevelopmentConfig()

    def func() -> Settings:
        return config

    return func()


configurations = find_which_config()


if __name__ == "__main__":
    print(configurations)
