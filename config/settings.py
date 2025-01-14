import os
from .utils import load_env

load_env()

class Config:
    # General Config
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')


class DevelopmentConfig(Config):
    DB_HOST = os.getenv('DEV_DB_HOST', 'localhost')
    DB_PORT = os.getenv('DEV_DB_PORT', '27017')


class TestingConfig(Config):
    DB_HOST = os.getenv('TEST_DB_HOST')
    DB_PORT = os.getenv('TEST_DB_PORT')
    DB_NAME = os.getenv('TEST_DB_NAME')
    DB_USER = os.getenv('TEST_DB_USER')
    DB_PASS = os.getenv('TEST_DB_PASS')

class ProductionConfig(Config):
    DB_HOST = os.getenv("PROD_DB_HOST")
    DB_PORT = os.getenv("PROD_DB_PORT")
    DB_NAME = os.getenv("PROD_DB_NAME")
    DB_USER = os.getenv("PROD_DB_USER")
    DB_PASS = os.getenv("PROD_DB_PASS")

def get_config():
    stage = os.getenv('STAGE', 'development').lower()
    if stage == 'development':
        return DevelopmentConfig
    elif stage == 'testing':
        return TestingConfig
    elif stage == 'production':
        return ProductionConfig
    else:
        raise ValueError(f'Unkown stage: {stage}')