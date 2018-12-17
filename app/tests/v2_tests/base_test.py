from unittest import TestCase

from app import create_app
from ...api.db_config import create_tables, destroy_tables


class BaseTest(TestCase):
    def setUp(self):
        self.app = create_app().test_client

        create_tables()

        self.incident = {
            "title": "Bad Roads in Kasarani",
            "incident": "intervention",
            "location": "-1.292066, 36.821945",
            "description": "Potholes on the road",
            "images": "pothole.jpg"
        }
        self.incident2 = {
            "title": "Corruption in Police Station",
            "incident": "intervention",
            "location": "-1.292066, 36.821945",
            "description": "Potholes on the road",
            "images": "pothole.jpg"
        }
        self.user = {

            "firstname": "Alex",
            "lastname": "Mwangi",
            "email": "Muriithi@gmail.com",
            "username": "muriithi",
            "phone": "98890",
            "password": "123qwwww3"
        }
        self.user2 = {
            "firstname": "Daniel",
            "lastname": "Gates",
            "email": "Muriithi@gmail.com",
            "username": "muriithi",
            "phone": "23445",
            "isAdmin": "false",
            "password": "12333"
        }
        self.user_login = {

            "username": "muriithi",
            "password": "123qwwww3"

        }

    def tearDown(self):
        destroy_tables()
