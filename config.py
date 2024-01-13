from datetime import timedelta

class Config:
    JWT_SECRET_KEY = "Muitas coisas podem ser poucas coisas"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=3)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=3)

class DevelopmentConfig(Config):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=3)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=3)
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:lukas@localhost:5432/banco_pix"

class TestConfig(Config):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=10)
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

config = {
    "development": DevelopmentConfig,
    "test": TestConfig
}