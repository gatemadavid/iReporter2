from ...db_config import init_db
import psycopg2.extras


class IncidentsModel():
    def __init__(self):
        self.db = init_db()

    def save(self, title, incident, location, status, description, createdBy):
        payload = {
            'title': title,
            'incident': incident,
            'location': location,
            'status': status,
            'description': description,
            'createdBy': createdBy
        }

        query = """INSERT INTO incidents (title, incident, location, status, description, createdBy) VALUES
            (%(title)s, %(incident)s, %(location)s, %(status)s, %(description)s, %(createdBy)s)"""

        curr = self.db.cursor()
        curr.execute(query, payload)
        self.db.commit()
        return payload

    def getIncidents(self):
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

    def getUserIncidents(self, username):
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


class IncidentModel():
    def __init__(self):
        self.db = init_db()

    def getIncident(self, id):
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
        createdBy = data['createdBy']
        resp = {
            "id": id,
            "title": title,
            "incident": incident,
            "location": location,
            "status": status,
            "description": description,
            "createdBy": createdBy,
        }
        return resp

    def deleteIncident(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""DELETE FROM incidents WHERE id=%s""", [id])
        self.db.commit()
        return {"Message": "Incident Deleted"}

    def updateIncident(self, id, title, incident, location, status, description, createdBy):
        dbconn = self.db
        curr = dbconn.cursor()
        # check status of incident
        curr.execute("""SELECT status FROM incidents where id=%s;""", [id])
        status = curr.fetchone()
        if status == "new":
            curr.execute("UPDATE incidents SET title=%s, incident=%s, location=%s, status=%s, description=%s, createdBy=%s WHERE id=%s",
                         (title, incident, location, status, description, createdBy, id))

            self.db.commit()
            return {"Message": "Incident Updated"}
        else:
            return {"Message": "Incident Cannot be Updated"}
