from flask_restful import Resource
from flask import jsonify, make_response, request
from ..models.Redflags import RedFlagsModel, SingleFlagModel


class RedFlags(Resource, RedFlagsModel):
    def __init__(self):
        self.db = RedFlagsModel()

    def post(self):
        data = request.get_json()
        title = data['title']
        description = data['description']
        location = data['location']
        incident_type = data['type']
        resp = self.db.save(title, description, location, incident_type)
        return make_response(jsonify({
            "message": "Red Flag Created",
            "Red Flags": resp
        }), 201)

    def get(self):
        resp = self.db.get_flags()
        return make_response(jsonify({
            "Message": "success",
            "Red Flags": resp
        }), 200)


class RedFlag(Resource, SingleFlagModel):
    def __init__(self):
        self.db = SingleFlagModel()

    def get(self, flag_id):
        resp = self.db.getSingleFlag(flag_id)
        return make_response(jsonify({
            "Message": "success",
            "Red Flags": resp
        }), 200)

    def delete(self, flag_id):
        self.db.deleteFlag(flag_id)
        return make_response(jsonify({
            "Message": "Flag Deleted"
        }), 204)
