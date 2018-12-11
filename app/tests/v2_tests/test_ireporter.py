import json
import unittest
from app import create_app
from ...api.db_config import test_tables, destroy_tables
users_url = "/api/v2/users"
user_login_url = "/api/v2/login"
incidents_url = "/api/v2/incidents"


class RedFlagsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()

        self.client = self.app.test_client

        test_tables()
        self.incident = {
            "title": "Corruption in Police HQ",
            "incident": "Red Flag",
            "location": "Kasarani PD",
            "status": "new",
            "description": "Bribing police",
            "createdBy": "David"
        }
        self.user = {
            "firstname": "MIKE",
            "lastname": "Muriithi",
            "email": "Muriithi@gmail.com",
            "username": "mike",
            "phone": "98890",
            "isAdmin": "false",
            "password": "12333"
        }
        self.user2 = {
            "firstname": "Daniel",
            "lastname": "Gates",
            "email": "Muriithi@gmail.com",
            "username": "mike123",
            "phone": "23445",
            "isAdmin": "false",
            "password": "12333"
        }
        self.user_login = {
            "username": "mikwwedd11llm1",
            "password": "12333"

        }

    def register_user(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        
    def get_token(self):
        res = self.client().post(user_login_url,
                                 data=json.dumps(self.user_login),
                                 headers={'content-type': "application/json"})
        self.assertEqual(res.status_code, 200)
        access_token = json.loads(res.data.decode)['token']
        print(access_token)
        return access_token

    def test_get_users(self):
        access_token = self.get_token()
        res = self.client().get(users_url, headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 200)

    def test_get_single_user(self):
        access_token = self.get_token()
        result = self.client().get("/api/v2/users/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 201)

    def test_delete_user(self):
        access_token = self.get_token()
        result = self.client().delete("/api/v2/users/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 200)

    def test_update_user(self):
        res = self.client().put(users_url, data=json.dumps(
            self.user2), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    #     # test incidents

    def test_incident_creation(self):
        access_token = self.get_token()
        res = self.client().post(incidents_url, data=json.dumps(
            self.incident),  headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_get_incidents(self):
        access_token = self.get_token()
        res = self.client().get(incidents_url, headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_get_single_incident(self):
        access_token = self.get_token()
        result = self.client().get("/api/v2/incidents/1",
                                   headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 201)

    def test_delete_incident(self):
        access_token = self.get_token()
        result = self.client().delete("/api/v2/incidents/1",
                                      headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 200)

    def test_update_incident(self):
        access_token = self.get_token()
        res = self.client().put(incidents_url, data=json.dumps(
            self.incident), headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def tearDown(self):
        destroy_tables()
