from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from werkzeug.security import generate_password_hash

from ..models.Users import UsersModel, UserModel

from ..models.Incidents import IncidentsModel
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
        raw_pass = data['password']
        password = generate_password_hash(raw_pass)

        user = self.db.registerUsers(username)
        if len(user) != 0:
            return make_response(jsonify({
                'Message': 'Username already exists'
            }), 202)

        else:
            self.db.save(firstname, lastname, email,
                         username, phone, isAdmin, password)
            return make_response(jsonify({
                "Message": "User Registered. Please login"
            }), 201)
    
    def get(self):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            users = self.db.getusers()
            return make_response(jsonify({
                "Users": users,
                "Message": "All Users"
            }), 200)
        else:

            abort(404)


class LoginView(Resource, UsersModel):
    def __init__(self):
        self.db = UsersModel()
        self.user_db = IncidentsModel()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        auth = self.db.authenticate(username, password)
        print(auth)
        return auth


class UserView(Resource, UserModel):
    def __init__(self):
        self.db = UserModel()

    def get(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            res = self.db.getUser(id)
            return make_response(jsonify({
                'Response': res
            }), 201)

    def delete(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            self.db.deleteUser(id)
            return {
                "Message": "User Deleted"
            }

    def put(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            data = request.get_json()
            firstname = data['firstname']
            lastname = data['lastname']
            email = data['email']
            username = data['username']
            phone = data['phone']
            isAdmin = data['isAdmin']
            password = data['password']

            self.db.updateUser(id, firstname, lastname, email,
                               username, phone, isAdmin, password)
            return make_response(jsonify({
                'Status': 'Ok',
                'Message': 'User Details Updated'
            }), 201)
