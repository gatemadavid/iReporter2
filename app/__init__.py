from flask import Flask
from .api.v1 import version1 as v1
from .api.v2 import version2 as v2
from .api.db_config import create_tables


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    create_tables()
    app.register_blueprint(v1)
    app.register_blueprint(v2)

    @app.errorhandler(404)
    def page_not_found(e):
        return 'The requested page does not exist. Kindly check your url'

    @app.errorhandler(403)
    def forbidden_access(e):
        return 'Access forbiden'

    @app.errorhandler(500)
    def internal_server_error(e):
        return 'An error occurred.'

    return app
