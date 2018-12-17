from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.Incidents import IncidentsModel
from ..models.Users import UsersModel
from app.api.validations.validations import Validations


class IncidentsView(Resource):
    def __init__(self):
        self.db = IncidentsModel()
        self.users = UsersModel()

    def get(self):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        else:
            res = self.db.get_incidents()

            return make_response(jsonify({
                'All Incidents': res
            }), 201)

    def post(self):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        elif access_token:
            user = self.users.decode_token(access_token)
            createdBy = str(user)
            data = request.get_json()
            resp = Validations().validate_incident_details(data, createdBy)
            if resp == str(resp):
                return make_response(jsonify({
                    "Message": resp
                }), 201)
            else:
                self.db.save(resp)
                return make_response(jsonify({
                    'Message': 'Incident Created'
                }), 201)


class IncidentView(Resource):
    def __init__(self):
        self.db = IncidentsModel()
        self.users = UsersModel()

    def get(self, id):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        else:
            res = self.db.get_one_incident(id)
            return make_response(jsonify({
                'Status': 'Ok',
                'My Incident': res
            }), 201)

    def delete(self, id):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        else:
            resp = self.db.delete_incident(id)
            return make_response(jsonify({
                'Message': resp
            }), 201)

    def put(self, id):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        elif access_token:
            user = self.users.decode_token(access_token)
            createdBy = str(user)
            data = request.get_json()
            resp = Validations().validate_incident_details(data, createdBy)
            if resp == str(resp):
                return make_response(jsonify({
                    "Message": resp
                }), 201)
            else:
                self.db.update_incident(id, resp)
                return make_response(jsonify({
                    'Message': 'Incident Updated'
                }), 201)


class UserIncidentsView(Resource):
    def __init__(self):
        self.db = IncidentsModel()
        self.users = UsersModel()

    def get(self):
        access_token = Validations().get_access_token()
        if not access_token:
            return jsonify({"Message": "Token needed. Please login"})
        else:
            user = self.users.decode_token(access_token)
            username = str(user)
            res = self.db.get_user_incidents(username)
            return make_response(jsonify({

                'My Incidents': res
            }), 201)
