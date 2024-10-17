from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_driver: str
    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_name: str
    date_format: str

    @property
    def database_url(self):
        return f"{self.db_driver}://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def date_format(self):
        return self.date_format

    class Config:
        env_file = ".env"


settings = Settings()
