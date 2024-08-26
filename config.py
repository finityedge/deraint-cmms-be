import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:franc123@localhost/cmmsdb_new'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/cmms_prod'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/cmms_test'