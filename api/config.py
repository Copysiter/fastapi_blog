from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    APP_NAME: str
    HOST: str
    PORT: int
    RELOAD: bool

    class Config:
        env_file = ".env"


settings = Settings()
