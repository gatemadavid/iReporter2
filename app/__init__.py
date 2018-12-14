from flask import Flask
from .api.v1 import version1 as v1
from .api.v2 import version2 as v2
from .api.db_config import create_tables
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    create_tables()
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app
