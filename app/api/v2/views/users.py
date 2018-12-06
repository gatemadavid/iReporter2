from flask_restful import Resource
from flask import jsonify, make_response, request
from werkzeug.security import generate_password_hash
from functools import wraps
from ..models.Users import UsersModel, UserModel
import os
secret_key = os.getenv('SECRET')


class UsersView(Resource, UsersModel):
    def __init__(self):
        self.db = UsersModel()

    def post(self):
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        username = data['username']
        phone = data['phone']
        isAdmin = data['isAdmin']
        password = data['password']
        # password = generate_password_hash(raw_pass)

        user = self.db.registerUsers(username)
        if len(user) < 0:
            return make_response(jsonify({
                'Message': 'Username already exists'
            }), 202)

        else:
            payload = self.db.save(firstname, lastname, email,
                                   username, phone, isAdmin, password)
            return make_response(jsonify({
                "Message": "User Registered. Please login"
            }), 201)

    def get(self):

        # users = self.db.getusers()
        # return make_response(jsonify({
        #     "Users": users,
        #     "Message": "All Users"
        # }), 200)

        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            users = self.db.getusers()
            return make_response(jsonify({
                "Users": users,
                "Message": "All Users"
            }), 200)
        else:
            return make_response(jsonify({
                "Message": "Invalid Token"
            }), 200)


class LoginView(Resource, UsersModel):
    def __init__(self):
        self.db = UsersModel()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        auth = self.db.authenticate(username, password)
        return auth


class UserView(Resource, UserModel):
    def __init__(self):
        self.db = UserModel()

    def get(self, id):
        res = self.db.getUser(id)
        return make_response(jsonify({
            'Response': res
        }), 201)

    def delete(self, id):
        self.db.deleteUser(id)
        return {
            "Message": "User Deleted"
        }

    def put(self, id):
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        username = data['username']
        phone = data['phone']
        isAdmin = data['isAdmin']
        password = data['password']

        result = self.db.updateUser(id, firstname, lastname, email,
                                    username, phone, isAdmin, password)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': 'User Details Updated'
        }), 201)
