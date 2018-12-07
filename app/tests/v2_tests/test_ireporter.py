import json
import unittest
from app import create_app
from ...api.db_config import create_tables, destroy_tables
users_url = "/api/v2/users"
user_login_url = "/api/v2/login"
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
            "username": "Davido",
            "phone": "98890",
            "isAdmin": "True",
            "password": "test1234"}

    def register_user(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user),  headers={'content-type': "application/json"})
        self.assertEqual(res.status_code, 201)

    def login_user(self, username="Davido", password="test1234"):

        user_data = {
            'username': username,
            'password': password
        }
        return self.client().post(user_login_url, data=json.dumps(
            user_data),  headers={'content-type': "application/json"})

    def test_get_users(self):
        self.register_user()
        res = self.login_user()
        access_token = json.loads(res.data.decode())['token']
        res = self.client().get(users_url, headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 200)

    def test_get_single_user(self):
        self.register_user()
        res = self.login_user()
        access_token = json.loads(res.data.decode())['token']
        self.assertEqual(res.status_code, 201)
        result = self.client().get("/api/v2/users/1")
        self.assertEqual(result.status_code, 201)

    # def test_delete_user(self):
    #     res = self.client().post(users_url, data=json.dumps(
    #         self.user), content_type='application/json')
    #     self.assertEqual(res.status_code, 201)
    #     result = self.client().delete("/api/v2/users/1")
    #     self.assertEqual(result.status_code, 200)

    # def test_update_user(self):
    #     res = self.client().post(users_url, data=json.dumps(
    #         self.user), content_type='application/json')
    #     self.assertEqual(res.status_code, 201)

    # def test_user_login(self):
    #     pass

    #     # test incidents

    def test_incident_creation(self):
        self.register_user()
        res = self.login_user()
        access_token = json.loads(res.data)['token']
        res = self.client().post(incidents_url, data=json.dumps(
            self.incident),  headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_get_incidents(self):
        self.register_user()
        res = self.login_user()
        access_token = json.loads(res.data.decode())['token']
        res = self.client().get(incidents_url, headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    # def test_get_single_incident(self):
    #     res = self.client().post(incidents_url, data=json.dumps(
    #         self.incident), content_type='application/json')
    #     self.assertEqual(res.status_code, 201)
    #     result = self.client().get("/api/v2/incidents/1")
    #     self.assertEqual(result.status_code, 201)

    # def test_delete_incident(self):
    #     res = self.client().post(incidents_url, data=json.dumps(
    #         self.incident), content_type='application/json')
    #     self.assertEqual(res.status_code, 201)
    #     result = self.client().delete("/api/v2/incidents/1")
    #     self.assertEqual(result.status_code, 200)

    # def test_update_incident(self):
    #     res = self.client().post(incidents_url, data=json.dumps(
    #         self.incident), content_type='application/json')
    #     self.assertEqual(res.status_code, 201)

    def tearDown(self):
        destroy_tables()
