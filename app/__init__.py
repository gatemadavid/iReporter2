from flask import Flask
from .api.v1 import version1 as v1
from .api.v2 import version2 as v2
from .api.db_config import create_tables


def create_app():
    app = Flask(__name__)
    create_tables()
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app
