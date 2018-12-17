from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.Users import UsersModel

from ..models.Incidents import IncidentsModel

from app.api.validations.validations import Validations


class UsersView(Resource):
    def __init__(self):
        self.db = UsersModel()

    def post(self):
        data = request.get_json()
        resp = Validations().validate_user_inputs(data)
        username = data['username']
        user = self.db.register_users(username)
        if len(user) != 0:
            return make_response(jsonify({
                'Message': 'Username already exists'
            }), 202)
        elif resp == str(resp):
            return make_response(jsonify({
                "Message": resp
            }), 201)
        else:
            self.db.save(resp)
            return make_response(jsonify({
                "Message": "User Registered. Please login"
            }), 201)

    def get(self):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        else:
            users = self.db.get_users()
            return make_response(jsonify({
                "Users": users,
                "Message": "All Users"
            }), 200)


class LoginView(Resource):
    def __init__(self):
        self.db = UsersModel()
        self.user_db = IncidentsModel()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        auth = self.db.authenticate(username, password)
        return auth


class UserView(Resource):
    def __init__(self):
        self.db = UsersModel()

    def get(self, id):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        else:
            res = self.db.get_single_user(id)
            return make_response(jsonify({
                'Response': res
            }), 201)

    def delete(self, id):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        else:
            self.db.delete_user(id)
            return {
                "Message": "User Deleted"
            }

    def put(self, id):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        if access_token:
            data = request.get_json()
            resp = Validations().validate_user_inputs(data)
            if resp == str(resp):
                return make_response(jsonify({
                    "Message": resp
                }), 201)
            else:
                self.db.update_user(id, resp)
                return make_response(jsonify({
                    'Message': 'User Details Updated'
                }), 201)
