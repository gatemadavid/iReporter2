from flask_restful import Api
from flask import Blueprint

from .views.users import UsersView, UserView, LoginView
from .views.incidents import IncidentsView, IncidentView, UserIncidentsView

version2 = Blueprint('api2', __name__, url_prefix='/api/v2')
api = Api(version2)

api.add_resource(UsersView, '/users')
api.add_resource(LoginView, '/login')
api.add_resource(UserView, '/users/<int:id>')
api.add_resource(IncidentsView, '/incidents')
api.add_resource(UserIncidentsView, '/dashboard')
api.add_resource(IncidentView, '/incidents/<int:id>')
