import psycopg2.extras
from datetime import datetime, timedelta
from ...db_config import init_db
from werkzeug.security import check_password_hash
import jwt
import os

secret_key = os.getenv('SECRET')
url = os.getenv('DATABASE_URL')


class UsersModel():
    def __init__(self):
        self.db = init_db()

    def save(self, firstname, lastname, email, username, phone, isAdmin, password):
        payload = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "username": username,
            "phone": phone,
            "isAdmin": isAdmin,
            "password": password
        }
        query = """INSERT INTO users (firstname, lastname, email, username, phone, isAdmin, password) VALUES
            (%(firstname)s, %(lastname)s, %(email)s, %(username)s, %(phone)s, %(isAdmin)s, %(password)s)"""
        curr = self.db.cursor()
        curr.execute(query, payload)
        self.db.commit()
        return payload

    def get_users(self):
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

    def register_users(self, username):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM users WHERE username=%s""", [username])
        data = curr.fetchall()
        return data

    def get_single_user(self, id):
        dbconn = self.db
        curr = dbconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        curr.execute(
            """SELECT * FROM users WHERE id=%s; """, [id])
        data = curr.fetchone()
        id = data['id']
        username = data['username']
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        phone = data['phone']
        resp = {
            "id": id,
            "firstname": firstname,
            "lastname": lastname,
            "username": username,
            "email": email,
            "phone": phone,
        }
        return resp

    def delete_user(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""DELETE FROM users WHERE id=%s""", [id])
        self.db.commit()
        return {"Message": "User Deleted"}

    def update_user(self, id, firstname, lastname, email, username, phone, isAdmin, password):
        dbconn = self.db
        curr = dbconn.cursor()

        curr.execute("UPDATE users SET firstname=%s, lastname=%s, email=%s, username=%s, phone=%s, isAdmin=%s, password=%s WHERE id=%s",
                     (firstname, lastname, email, username, phone, isAdmin, password, id))

        self.db.commit()
        return {"Message": "User Updated"}

    def authenticate(self, username, password):
        dbconn = self.db
        curr = dbconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        curr.execute(
            """SELECT password, isAdmin FROM users WHERE username=%s""", [username])
        data = curr.fetchone()
        db_pass = data['password']
        db_password = str.strip(db_pass)
        is_admin = data[1]
        if check_password_hash(db_password, password):
            jwt_string = {
                'exp': datetime.utcnow() + timedelta(minutes=30),
                'iat': datetime.utcnow(),
                'user': username,
                "admin": is_admin
            }
            auth_token = jwt.encode(jwt_string, secret_key, algorithm='HS256')
            token = auth_token.decode('UTF-8')
            return {"token": token, "Message": "Login Successful"}

        else:
            return {"message": "Username or Password Incorrect"}

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, secret_key)
            username = payload['user']
            is_admin = payload['admin']
            print(is_admin)
            return username
        except jwt.ExpiredSignatureError:
            return {"message": 'Token Expired. Please log in again.'}
        except jwt.InvalidTokenError:
            return {"Message": 'Invalid token. Please log in again.'}

    # def token_required(f):
    #     @wraps(f)
    #     def decorated(*args, **kwargs):
    #         token = None
    #         if
