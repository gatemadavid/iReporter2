from flask import Blueprint
from flask_restful import Api

from .views.redflags import RedFlags, RedFlag
from .views.users import Users, User
version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)
api.add_resource(RedFlags, '/redflags')  # get all flags
api.add_resource(RedFlag, '/redflags/<int:flag_id>')  # get one flag
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')
