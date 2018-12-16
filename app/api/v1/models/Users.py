
users_db = []


class UsersModel():
    def __init__(self):
        self.users = users_db

    def saveUser(self, data):
        user_id = len(users_db) + 1
        user_data = {
            "id": user_id,
            "fname": data['fname'],
            "lname":  data['lname'],
            "email": data['email'],
            "password": data['password'],
            "isAdmin": data['isAdmin']
        }
        self.users.append(user_data)
        return self.users

    def get_users(self):
        return self.users

    def getUser(self, user_id):
        for user in users_db:
            if user['id'] == user_id:
                return user

    def deleteUser(self, user_id):
        for user in users_db:
            if user['id'] == user_id:
                return users_db.remove(user)

    def updateUser(self, user_id, data):
        for user in users_db:
            if user['id'] == user_id:
                user['fname'] = data['fname']
                user['lname'] = data['lname']
                user['email'] = data['email']
                user['password'] = data['password']
                user['isAdmin'] = data['isAdmin']
                return user
