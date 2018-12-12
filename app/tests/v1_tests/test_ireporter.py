import json
import unittest
from app import create_app


redflags_url = "/api/v1/redflags"
redflag_url = "/api/v1/redflags/<int:id>"
users_url = "/api/v1/users"


class RedFlagsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

        self.payload = {
            "id": "1",
            "title": "corruption",
            "description": "Bribery",
            "location": "Ruiru",
            "type": "red flag",
            "status": "new",
            "images": "images"
        }
        self.data = {
            "id": "1",
            "description": "Bribing police officers",
            "location": "Ruiru",
            "status": "new"
        }
        self.user_data = {
            "id": "1",
            "firstname": "David",
            "lastname": "Muriithi",
            "username": "mufasa21",
            "email": "muriithi@gmail.com",
            "password": "david123",
            "is_admin": "false"
        }
        self.user2_data = {
            "id": "1",
            "firstname": "Mercy",
            "lastname": "Muriithi",
            "username": "Wangari2018",
            "email": "wanga@gmail.com",
            "password": "wanga1234",
            "is_admin": "true"
        }
        self.client = self.app.test_client

    def test_create_redflag(self):
        res = self.client().post(redflags_url, data=json.dumps(
            self.payload),  headers={'content-type': "application/json"})
        data = json.loads(res.get_data())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['message'], "Red Flag Created")

    def test_get_all_redflags(self):
        res = self.client().post(redflags_url, headers={
            'Content-Type': 'application/json'}, data=json.dumps(self.payload))
        res = self.client().get(redflags_url)
        self.assertEqual(res.status_code, 200)

    def test_get_single_redflag(self):
        res = self.client().post(redflags_url, data=json.dumps(
            self.payload), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client().get("/api/v1/redflags/1")
        self.assertEqual(result.status_code, 200)

    def test_edit_redflag(self):
        res = self.client().post(redflags_url, data=json.dumps(self.payload),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)

        res_put = self.client().put('/api/v1/redflags/1',
                                    data=json.dumps(self.data),
                                    content_type='application/json')
        self.assertEqual(res_put.status_code, 200)

    def test_delete_redflag(self):
        res = self.client().post(redflags_url, data=json.dumps(
            self.payload), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client().delete("/api/v1/redflags/1")
        self.assertEqual(result.status_code, 200)

    # test users

    def test_user_creation(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user_data),  content_type='application/json')
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.get_data())
        self.assertEqual(data['message'], "User Created")

    def test_get_all_users(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user_data), content_type='application/json')
        res = self.client().get(redflags_url)
        self.assertEqual(res.status_code, 200)

    def test_get_single_user(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user_data), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_delete_user(self):
        res = self.client().post(users_url, data=json.dumps(
            self.user_data), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        result = self.client().delete("/api/v1/users/1")
        self.assertEqual(result.status_code, 200)
        resp = json.loads(result.get_data())
        self.assertEqual(resp['Message'], "User Deleted")

    def test_edit_user(self):
        res = self.client().post(users_url, data=json.dumps(self.user_data),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)

        res_put = self.client().put('/api/v1/users/1',
                                    data=json.dumps(self.user2_data),
                                    content_type='application/json')
        self.assertEqual(res_put.status_code, 200)


if __name__ == "__main__":
    unittest.main()
