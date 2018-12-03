from flask_restful import Resource
from flask import jsonify, make_response, request
from ..models.Users import UsersModel, UserModel


class Users(Resource, UsersModel):
    def __init__(self):
        self.users_db = UsersModel()

    def post(self):
        data = request.get_json()
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        password = data['password']
        is_admin = data['password']
        resp = self.users_db.saveUser(
            fname, lname, email, password, is_admin)
        return make_response(jsonify({
            "message": "User Created",
            "Users": resp
        }), 201)

    def get(self):
        resp = self.users_db.get_users()
        return make_response(jsonify({
            "message": "success",
            "Users": resp
        }), 200)


class User(Resource, UserModel):
    def __init__(self):
        self.users_db = UserModel()

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
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        password = data['password']
        is_admin = data['password']
        resp = self.users_db.updateUser(
            user_id, fname, lname, email, password, is_admin)
        return make_response(jsonify({
            "Status": 200,
            "Message": "Incident updated",
            "data": resp
        }), 200)
