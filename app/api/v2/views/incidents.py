from flask_restful import Resource
from flask import jsonify, make_response, request, abort

from ..models.Incidents import IncidentsModel
from ..models.Users import UsersModel


class IncidentsView(Resource):
    def __init__(self):
        self.db = IncidentsModel()
        self.users = UsersModel()

    def get(self):
        try:
            auth_header = request.headers.get('Authorization')
            access_token = auth_header.split(" ")[1]
            if access_token:
                res = self.db.get_incidents()

                return make_response(jsonify({
                    'All Incidents': res
                }), 201)
            else:
                abort(500)
        except ValueError:
            abort(500)

    def post(self):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            user = self.users.decode_token(access_token)
            createdBy = str(user)
            data = request.get_json()
            title = data['title']
            incident = data['incident']
            location = data['location']
            description = data['description']
            images = data['images']
            self.db.save(title, incident, location,
                         description, images, createdBy)
            return make_response(jsonify({
                'Message': 'Incident Created'
            }), 201)


class IncidentView(Resource):
    def __init__(self):
        self.db = IncidentsModel()

    def get(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            res = self.db.get_one_incident(id)
            return make_response(jsonify({
                'Status': 'Ok',
                'My Incident': res
            }), 201)

    def delete(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            resp = self.db.delete_incident(id)
            return make_response(jsonify({
                'Message': resp
            }), 201)

    def put(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            data = request.get_json()
            title = data['title']
            incident = data['incident']
            location = data['location']
            description = data['description']
            images = data['images']

            resp = self.db.update_incident(id, title, incident, location,
                                           description, images)
            return make_response(jsonify({
                'Message': resp
            }), 201)


class UserIncidentsView(Resource):
    def __init__(self):
        self.db = IncidentsModel()
        self.users = UsersModel()

    def get(self):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]

        if access_token:
            user = self.users.decode_token(access_token)
            username = str(user)
            res = self.db.get_user_incidents(username)
            return make_response(jsonify({

                'My Incidents': res
            }), 201)
