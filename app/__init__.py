from flask import Flask
from .extensions import db, migrate
from .api import api

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Tenant, Asset  # Import all your models here
    
    api.init_app(app)

    return app