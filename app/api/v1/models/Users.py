import re
users_db = []


class UsersModel():
    def __init__(self):
        self.users = users_db

    def save(self, payload):
        user_id = len(users_db) + 1
        user_data = {
            "id": user_id,
            "firstname": payload['firstname'],
            "lastname": payload['lastname'],
            "username": payload['username'],
            "email": payload['email'],
            "password": payload['password'],
            "is_admin": payload['is_admin']
        }
        self.users.append(user_data)
        return self.users

    def get_users(self):
        return self.users

    def get_user(self, user_id):
        for user in users_db:
            if user['id'] == user_id:
                return user

    def delete_user(self, user_id):
        for user in users_db:
            if user['id'] == user_id:
                return users_db.remove(user)

    def update_user(self, user_id, payload):
        for user in users_db:
            if user['id'] == user_id:
                user['firstname'] = payload['firstname']
                user['lastname'] = payload['lastname']
                user['email'] = payload['email']
                user['password'] = payload['password']
                user['isAdmin'] = payload['isAdmin']
                return user

    def validate_username(self, username):
        if len(username) < 7:
            return False
        elif not re.match("^[a-zA-Z0-9_.-]+$", username):
            return False
        else:
            return True

    def validate_email(self, email):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return True
        else:
            return False
