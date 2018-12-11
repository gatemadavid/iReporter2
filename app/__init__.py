from flask import Flask
from .api.v1 import version1 as v1
from .api.v2 import version2 as v2
# from .api.auth import auth_bluepint
from .api.db_config import create_tables
# from instance.config import app_config


def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'mysecretkey'
    create_tables()
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    # app.register_blueprint(auth_bluepint)
    return app
