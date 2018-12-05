import json
import unittest
from app import create_app
from ...api.db_config import create_tables, destroy_tables

users_url = "/api/v2/users"
incidents_url = "/api/v2/incidents"


class RedFlagsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        create_tables()
        self.incident = {
            "title": "Corruption in Police HQ",
            "incident": "Red Flag",
            "location": "Kasarani PD",
            "status": "new",
            "description": "Bribing police",
            "createdBy": "David"
        }
        self.user = {
            "firstname": "David",
            "lastname": "Muriithi",
            "email": "Muriithi@gmail.com",
            "username": "Dmuriithi",
            "phone": "98890",
            "isAdmin": "True"}

    def test_user_creation(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user),  headers={'content-type': "application/json"})
        self.assertEqual(res.status_code, 201)

    def test_get_users(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user),  headers={'content-type': "application/json"})
        res = self.client().get(users_url)
        self.assertEqual(res.status_code, 200)

    def test_get_single_user(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client().get("/api/v2/users/1")
        self.assertEqual(result.status_code, 201)

    def test_delete_user(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client().delete("/api/v2/users/1")
        self.assertEqual(result.status_code, 200)

    def test_update_user(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    # test incidents

    def test_incident_creation(self):
        res = self.client().post(incidents_url, data=json.dumps(
            self.incident),  headers={'content-type': "application/json"})
        self.assertEqual(res.status_code, 201)

    def test_get_incidents(self):
        res = self.client().post(incidents_url, data=json.dumps(
            self.incident),  headers={'content-type': "application/json"})
        res = self.client().get(users_url)
        self.assertEqual(res.status_code, 200)

    def test_get_single_incident(self):
        res = self.client().post(incidents_url, data=json.dumps(
            self.incident), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client().get("/api/v2/incidents/1")
        self.assertEqual(result.status_code, 201)

    def test_delete_incident(self):
        res = self.client().post(incidents_url, data=json.dumps(
            self.user), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client().delete("/api/v2/incidents/1")
        self.assertEqual(result.status_code, 200)

    def test_update_incident(self):
        res = self.client().post(incidents_url, data=json.dumps(
            self.incident), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def tearDown(self):
        destroy_tables()
