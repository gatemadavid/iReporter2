from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.Incidents import IncidentsModel, IncidentModel
from ..models.Users import UsersModel


class IncidentsView(Resource, IncidentsModel):
    def __init__(self):
        self.db = IncidentsModel()
        self.users = UsersModel()

    def get(self):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            res = self.db.getIncidents()

            return make_response(jsonify({
                'Status': 'Ok',
                'My Incidents': res
            }), 201)

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
            status = data['status']
            description = data['description']
            # createdBy = data['createdBy']
            self.db.save(title, incident, location,
                         status, description, createdBy)
            return make_response(jsonify({
                'Status': 'Ok',
                'Message': 'Incident Created'
            }), 201)


class IncidentView(Resource, IncidentModel):
    def __init__(self):
        self.db = IncidentModel()

    def get(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            res = self.db.getIncident(id)
            return make_response(jsonify({
                'Status': 'Ok',
                'My Incident': res
            }), 201)

    def delete(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            self.db.deleteIncident(id)
            return {
                "Message": "Incident Deleted"
            }

    def put(self, id):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            data = request.get_json()
            title = data['title']
            incident = data['incident']
            location = data['location']
            status = data['status']
            description = data['description']
            createdBy = data['createdBy']
            self.db.updateIncident(id, title, incident, location,
                                   status, description, createdBy)
            return make_response(jsonify({
                'Status': 'Ok',
                'Message': 'Incident Updated'
            }), 201)


class UserIncidentsView(Resource, IncidentsModel):
    def __init__(self):
        self.db = IncidentsModel()
        self.users = UsersModel()

    def get(self):
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]

        if access_token:
            user = self.users.decode_token(access_token)
            username = str(user)
            res = self.db.getUserIncidents(username)
            return make_response(jsonify({
                'Status': 'Ok',
                'My Incidents': res
            }), 201)
