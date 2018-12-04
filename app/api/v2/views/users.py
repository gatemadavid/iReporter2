from flask_restful import Resource
from flask import jsonify, make_response, request
from ..models.Users import UsersModel


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

        payload = self.db.save(firstname, lastname, email,
                               username, phone, isAdmin)
        return make_response(jsonify({
            "Message": "User Created",
            "User": payload
        }), 201)

    def get(self):
        users = self.db.getusers()
        return make_response(jsonify({
            "Users": users,
            "Message": "All Users"
        }), 200)
