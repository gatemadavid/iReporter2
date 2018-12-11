from flask_restful import Resource
from flask import jsonify, make_response, request
from ..models.Users import UsersModel


class Users(Resource):
    def __init__(self):
        self.users_db = UsersModel()

    def post(self):
        data = request.get_json()
        fname = data['firstname']
        lname = data['lastname']
        uname = data['username']
        raw_email = data['email']
        password = data['password']
        is_admin = data['isAdmin']
        valid_username = self.users_db.validate_username(uname)
        valid_email = self.users_db.validate_email(raw_email)

        if not valid_username:
            return {"Username should not be less than 7 characters"}

        elif not valid_email:
            return {"Please enter a valid email"}
        else:
            payload = {
                "firstname": fname,
                "lastname": lname,
                "username": uname,
                "email": raw_email,
                "password": password,
                "is_admin": is_admin
            }
            print(payload)
        self.users_db.save(payload)
        return make_response(jsonify({
            "message": "User Created",
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
        resp = self.users_db.get_user(user_id)
        return make_response(jsonify({
            "Message": "success",
            "User": resp
        }), 200)

    def delete(self, user_id):
        self.users_db.delete_user(user_id)
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
        resp = self.users_db.update_user(
            user_id, fname, lname, email, password, is_admin)
        return make_response(jsonify({
            "Status": 200,
            "Message": "Incident updated",
            "data": resp
        }), 200)
