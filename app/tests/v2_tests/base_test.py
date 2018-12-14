from unittest import TestCase

from app import create_app
from ...api.db_config import create_tables, destroy_tables


class BaseTest(TestCase):
    def setUp(self):
        self.app = create_app('testing').test_client

        create_tables()

        self.incident = {
            "title": "Corruption in Police",
            "incident": "Redflag",
            "location": "Ronald Ngala Street",
            "description": "Potholes on the road",
            "images": "pothole.jpg"
        }
        self.incident2 = {
            "title": "Corruption in Lands ministry",
            "incident": "intervention",
            "location": "Ardhi house",
            "description": "Bribing officials",
            "images": "corrupt.jpg"
        }
        self.user = {

            "firstname": "Alex",
            "lastname": "Mwangi",
            "email": "Muriithi@gmail.com",
            "username": "muriithi",
            "phone": "98890",
            "isAdmin": "false",
            "password": "1233"
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
            "password": "1233"

        }

    def tearDown(self):
        destroy_tables()
