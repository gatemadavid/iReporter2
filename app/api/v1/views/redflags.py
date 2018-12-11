from flask_restful import Resource
from flask import jsonify, make_response, request
from ..models.Redflags import RedFlagsModel


class RedFlags(Resource):
    def __init__(self):
        self.db = RedFlagsModel()

    def post(self):
        data = request.get_json()
        title = data['title']
        description = data['description']
        location = data['location']
        images = data['images']
        status = data['status']
        incident_type = data['type']
        data = {
            "title": title,
            "description": description,
            "location": location,
            "incident_type": incident_type,
            "status": status,
            "images": images
        }
        self.db.save(data)
        return make_response(jsonify({
            "message": "Red Flag Created"
        }), 201)

    def get(self):
        resp = self.db.get_flags()
        return make_response(jsonify({
            "Red Flags": resp
        }), 200)


class RedFlag(Resource):
    def __init__(self):
        self.db = RedFlagsModel()

    def get(self, flag_id):
        resp = self.db.get_single_flag(flag_id)
        return make_response(jsonify({
            "Message": "success",
            "Red Flags": resp
        }), 200)

    def delete(self, flag_id):
        self.db.delete_flag(flag_id)
        return {
            "Message": "Flag Deleted"
        }

    def put(self, flag_id):
        data = request.get_json()
        description = data['description']
        location = data['location']
        resp = self.db.update_flag(flag_id, description, location)
        return make_response(jsonify({
            "Status": 200,
            "Message": "Incident updated",
            "data": resp
        }), 200)
