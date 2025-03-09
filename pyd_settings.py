#  pip install pydantic-settings
import os
from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict

os.environ["PRODUCTION_AUTH_KEY"] = "iugyfhgjjkhjvhg"
os.environ["PRODUCTION_MY_API_KEY"] = "iugyfhjhg"
os.environ["PRODUCTION_ENV2"] = "https://osdjfhiob.com"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_prefix="production_",
        env_file_encoding="utf-8",
        extra="ignore",                 # allow, forbid
        )

    service_name: str = Field(default="default")
    auth_key: str = Field(...,)
    api_key: str = Field(alias="my_api_key")
    url: str = Field(validation_alias=AliasChoices("env1", "env2"))


print(Settings().model_dump())
