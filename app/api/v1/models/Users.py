
users_db = []


class UsersModel():
    def __init__(self):
        self.users = users_db

    def saveUser(self, fname, lname, email, password, is_admin):
        user_id = len(users_db) + 1
        user_data = {
            "id": user_id,
            "fname": fname,
            "lname": lname,
            "email": email,
            "password": password,
            "is_admin": is_admin
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

    def updateUser(self, user_id, fname, lname, email, password, isAdmin):
        for user in users_db:
            if user['id'] == user_id:
                user['fname'] = fname
                user['lname'] = lname
                user['email'] = email
                user['password'] = password
                user['isAdmin'] = isAdmin
                return user
