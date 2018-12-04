from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.Incidents import IncidentsModel


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
            'My Incidents': result
        }), 201)
