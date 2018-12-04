from ...db_config import init_db


class UsersModel():
    def __init__(self):
        self.db = init_db()

    def save(self, firstname, lastname, email, username, phone, isAdmin):
        payload = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "username": username,
            "phone": phone,
            "isAdmin": isAdmin
        }
        query = """INSERT INTO users (firstname, lastname, email, username, phone, isAdmin) VALUES
            (%(firstname)s, %(lastname)s, %(email)s, %(username)s, %(phone)s, %(isAdmin)s)"""
        curr = self.db.cursor()
        curr.execute(query, payload)
        self.db.commit()
        return payload

    def getusers(self):
        conn = self.db
        curr = conn.cursor()
        curr.execute("""SELECT id, firstname, lastname, email, username, phone, isAdmin, registered FROM users""")
        data = curr.fetchall()
        response = []
        for i, users in enumerate(data):
            id, firstname, lastname, email, username, phone, isAdmin, registered = users
            data = dict(
                id=int(id),
                firstname=firstname,
                lastname=lastname,
                email=email,
                username=username,
                phone=phone,
                isAdmin=isAdmin,
                registered=registered
            )
            response.append(data)
        return response
