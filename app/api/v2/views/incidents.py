from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.Incidents import IncidentsModel, IncidentModel


class IncidentsView(Resource, IncidentsModel):
    def __init__(self):
        self.db = IncidentsModel()

    def get(self):
        res = self.db.getIncidents()

        return make_response(jsonify({
            'Status': 'Ok',
            'My Incidents': res
        }), 201)

    def post(self):
        data = request.get_json()
        title = data['title']
        incident = data['incident']
        location = data['location']
        status = data['status']
        description = data['description']
        createdBy = data['createdBy']

        result = self.db.save(title, incident, location,
                              status, description, createdBy)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': 'Incident Created'
        }), 201)


class IncidentView(Resource, IncidentModel):
    def __init__(self):
        self.db = IncidentModel()

    def get(self, id):
        res = self.db.getIncident(id)
        return make_response(jsonify({
            'Status': 'Ok',
            'My Incident': res
        }), 201)

    def delete(self, id):
        self.db.deleteIncident(id)
        return {
            "Message": "Incident Deleted"
        }

    def put(self, id):
        data = request.get_json()
        title = data['title']
        incident = data['incident']
        location = data['location']
        status = data['status']
        description = data['description']
        createdBy = data['createdBy']

        result = self.db.updateIncident(id, title, incident, location,
                                        status, description, createdBy)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': 'Incident Updated'
        }), 201)
