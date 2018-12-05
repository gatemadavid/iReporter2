from ...db_config import init_db


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


class IncidentModel():
    def __init__(self):
        self.db = init_db()

    def getIncident(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute(
            """SELECT id, title, incident, location, status, description, createdBy FROM incidents where id=%s; """, [id])
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

    def deleteIncident(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""DELETE FROM incidents WHERE id=%s""", [id])
        self.db.commit()
        return {"Message": "Incident Deleted"}

    def updateIncident(self, id, title, incident, location, status, description, createdBy):
        dbconn = self.db
        curr = dbconn.cursor()

        curr.execute("UPDATE incidents SET title=%s, incident=%s, location=%s, status=%s, description=%s, createdBy=%s WHERE id=%s",
                     (title, incident, location, status, description, createdBy, id))

        self.db.commit()
        return {"Message": "Incident Updated"}
