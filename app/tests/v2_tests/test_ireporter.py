import json
from .base_test import BaseTest
from ...api.db_config import destroy_tables

users_url = "/api/v2/users"
user_login_url = "/api/v2/login"
incidents_url = "/api/v2/incidents"


class RedFlagsTestCase(BaseTest):

    def test_register_user(self):
        resp = self.app().post('/api/v2/users', data=json.dumps(
            self.user), content_type='application/json')
        result = json.loads(resp.get_data())
        self.assertEqual(result['Message'], "User Registered. Please login")
        self.assertEqual(resp.status_code, 201)

    def test_login_user(self):
        resp = self.app().post('/api/v2/login',
                               data=json.dumps(self.user_login),
                               headers={'content-type': "application/json"})
        self.assertEqual(resp.status_code, 200)
        access_token = json.loads(resp.data)['token']
        return access_token

    def test_get_users(self):
        access_token = self.test_login_user()
        res = self.app().get(users_url, headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 200)

    def test_get_single_user(self):
        access_token = self.test_login_user()
        result = self.app().get("/api/v2/users/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 201)

    def test_update_user(self):
        access_token = self.test_login_user()
        res = self.app().put('/api/v2/users/1', data=json.dumps(
            self.user2), content_type='application/json',
            headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_delete_user(self):
        access_token = self.test_login_user()
        result = self.app().delete("/api/v2/users/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 200)

    # # test incidents

    def test_incident_creation(self):
        access_token = self.test_login_user()
        res = self.app().post('/api/v2/incidents', data=json.dumps(
            self.incident), content_type='application/json',
            headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_get_incidents(self):
        access_token = self.test_login_user()
        res = self.app().get(incidents_url, headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_get_single_incident(self):
        access_token = self.test_login_user()
        result = self.app().get("/api/v2/incidents/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 201)

    def test_update_incident(self):
        access_token = self.test_login_user()
        res = self.app().put('/api/v2/incidents/1', data=json.dumps(
            self.incident2), content_type='application/json',
            headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_delete_incident(self):
        access_token = self.test_login_user()
        result = self.app().delete("/api/v2/incidents/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        destroy_tables()
