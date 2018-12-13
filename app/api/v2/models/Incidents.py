from ...db_config import init_db
import psycopg2.extras


class IncidentsModel():
    def __init__(self):
        self.db = init_db()

    def save(self, title, incident, location, description, images, createdBy):
        payload = {
            'title': title,
            'incident': incident,
            'location': location,
            'description': description,
            'images': images,
            'createdBy': createdBy
        }

        query = """INSERT INTO incidents (title, incident, location, description, images, createdBy) VALUES
            (%(title)s, %(incident)s, %(location)s, %(description)s, %(images)s, %(createdBy)s)"""

        curr = self.db.cursor()
        curr.execute(query, payload)
        self.db.commit()
        return payload

    def get_incidents(self):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute(
            """SELECT id, title, incident, location, status, description, createdBy FROM incidents;""")
        data = curr.fetchall()
        resp = []
        for i, incidents in enumerate(data):
            id, title, incident, location, status, description, createdBy = incidents
            res = dict(
                id=int(id),
                title=title,
                incident=incident,
                location=location,
                status=status,
                description=description,
                createdBy=createdBy

            )
            resp.append(res)
        return resp

    def get_user_incidents(self, username):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute(
            """SELECT id, title, incident, location, status, description FROM incidents WHERE createdBy =%s;""", [username])
        data = curr.fetchall()
        resp = []
        for i, incidents in enumerate(data):
            id, title, incident, location, status, description = incidents
            res = dict(
                id=int(id),
                title=title,
                incident=incident,
                location=location,
                status=status,
                description=description
            )
            resp.append(res)
        return resp

    def get_one_incident(self, id):
        dbconn = self.db
        curr = dbconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        curr.execute(
            """SELECT id, title, incident, location, status, description, createdBy FROM incidents where id=%s; """, [id])
        data = curr.fetchone()
        id = data['id']
        title = data['title']
        incident = data['incident']
        location = data['location']
        status = data['status']
        description = data['description']

        resp = {
            "id": id,
            "title": title,
            "incident": incident,
            "location": location,
            "status": status,
            "description": description,

        }
        return resp

    def delete_incident(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""DELETE FROM incidents WHERE id=%s""", [id])
        self.db.commit()
        return ("Incident Deleted")

    def update_incident(self, id, title, incident, location, description, images):
        curr = self.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        curr.execute("""SELECT status FROM incidents where id=%s;""", [id])
        resp = curr.fetchone()
        data = resp['status']
        status = str.strip(data)
        if status != "Draft":
            return ("Incident Cannot be Updated")
        else:
            curr.execute("UPDATE incidents SET title=%s, incident=%s, location=%s, description=%s, images=%s WHERE id=%s",
                         (title, incident, location, description, images, id))
            self.db.commit()
            return ("Incident Has Been Updated")
