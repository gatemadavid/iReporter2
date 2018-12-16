from flask_restful import Resource
from flask import jsonify, make_response, request
from ..models.Users import UsersModel


class Users(Resource):
    def __init__(self):
        self.users_db = UsersModel()

    def post(self):
        data = request.get_json()
        self.users_db.saveUser(data)
        return make_response(jsonify({
            "message": "User Created"
        }), 201)

    def get(self):
        resp = self.users_db.get_users()
        return make_response(jsonify({
            "message": "success",
            "Users": resp
        }), 200)


class User(Resource):
    def __init__(self):
        self.users_db = UsersModel()

    def get(self, user_id):
        resp = self.users_db.getUser(user_id)
        return make_response(jsonify({
            "Message": "success",
            "User": resp
        }), 200)

    def delete(self, user_id):
        self.users_db.deleteUser(user_id)
        return make_response(jsonify({
            "Message": "User Deleted"
        }), 204)

    def put(self, user_id):
        data = request.get_json()
        self.users_db.updateUser(user_id, data)
        return make_response(jsonify({
            "Status": 200,
            "Message": "User updated",

        }), 200)
