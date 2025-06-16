from typing import Literal

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class DB(BaseSettings):
    user: str
    password: str
    host: str
    port: int

    @property
    def database_url(self) -> str:
        raise ...


class PG(DB):
    db_name: str = "postgresql"
    db: str

    @property
    def database_url(self) -> str:
        return f"{self.db_name}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    environment: Literal["DEV"] | Literal["PROD"] = "DEV"
    project_name: str
    project_host: str
    project_port: int
    secret_key: str
    # pg: PG

    @property
    def debug(self) -> bool:
        return self.environment == "DEV"


if __name__ == "__main__":
    print(Config().model_dump())
