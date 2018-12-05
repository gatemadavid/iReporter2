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
        curr.execute(
            """SELECT id, firstname, lastname, email, username, phone, isAdmin, registered FROM users""")
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


class UserModel():

    def __init__(self):
        self.db = init_db()

    def getUser(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute(
            """SELECT id, firstname, lastname, email, username, phone, isAdmin, registered FROM users WHERE id=%s; """, [id])
        data = curr.fetchone()
        # resp = []
        # for i, incident in enumerate(data):
        #     id, title, incident, location, status, description, createdBy = incident
        #     res = dict(
        #         id=int(id),
        #         title=title,
        #         incident=incident,
        #         location=location,
        #         status=status,
        #         description=description,
        #         createdBy=createdBy

        #     )
        #     resp.append(res)
        return data

    def deleteUser(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""DELETE FROM users WHERE id=%s""", [id])
        self.db.commit()
        return {"Message": "User Deleted"}

    def updateIncident(self, id, firstname, lastname, email, username, phone, isAdmin):
        dbconn = self.db
        curr = dbconn.cursor()

        curr.execute("UPDATE users SET firstname=%s, lastname=%s, email=%s, username=%s, phone=%s, isAdmin=%s WHERE id=%s",
                     (firstname, lastname, email, username, phone, isAdmin, id))

        self.db.commit()
        return {"Message": "User Updated"}
