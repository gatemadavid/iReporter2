import json
from .base_test import BaseTest


class RedFlagsTestCase(BaseTest):

    def test_register_user(self):
        resp = self.app().post('/api/v2/users', data=json.dumps(
            self.user), content_type='application/json')
        result = json.loads(resp.get_data())
        self.assertEqual(result['Message'], "User Registered. Please login")
        self.assertEqual(resp.status_code, 201)

    def test_duplicate_user_register(self):
        self.test_register_user()
        res = self.app().post('/api/v2/users', data=json.dumps(
            self.user), content_type='application/json')
        resp = json.loads(res.get_data())
        self.assertEqual(resp['Message'], "Username already exists")

    def test_login_user(self):
        self.app().post('/api/v2/users', data=json.dumps(
            self.user), content_type='application/json')
        resp = self.app().post('/api/v2/login',
                               data=json.dumps(self.user_login),
                               headers={'content-type': "application/json"})
        self.assertEqual(resp.status_code, 200)
        access_token = json.loads(resp.data)['token']
        return access_token

    def test_get_users(self):
        access_token = self.test_login_user()
        res = self.app().get('/api/v2/users/', headers=dict(
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
        self.app().post('/api/v2/users', data=json.dumps(
            self.user), content_type='application/json')
        result = self.app().delete("/api/v2/users/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 200)

    # # # test incidents

    def test_incident_creation(self):
        access_token = self.test_login_user()
        res = self.app().post('/api/v2/incidents', data=json.dumps(
            self.incident), content_type='application/json',
            headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_get_incidents(self):
        access_token = self.test_login_user()
        res = self.app().get('/api/v2/incidents', headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_get_single_incident(self):
        access_token = self.test_login_user()
        self.test_incident_creation()
        result = self.app().get("/api/v2/incidents/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 201)

    def test_update_incident(self):
        access_token = self.test_login_user()
        self.test_incident_creation()
        res = self.app().put('/api/v2/incidents/1', data=json.dumps(
            self.incident2), content_type='application/json',
            headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(res.status_code, 201)

    def test_delete_incident(self):
        access_token = self.test_login_user()
        self.test_incident_creation()
        result = self.app().delete("/api/v2/incidents/1", headers=dict(
            Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 201)
