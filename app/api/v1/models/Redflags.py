
red_flags = []


class RedFlagsModel():
    def __init__(self):
        self.db = red_flags

    def save(self, title, description, location, incident_type):
        id = len(red_flags) + 1
        payload = {
            "id": id,
            "title": title,
            "description": description,
            "location": location,
            "type": incident_type
        }
        self.db.append(payload)
        return self.db

    def get_flags(self):
        return self.db

    def getSingleFlag(self, flag_id):
        for flag in red_flags:
            if flag['id'] == flag_id:
                return flag

    def deleteFlag(self, flag_id):
        for flag in red_flags:
            if flag['id'] == flag_id:
                return red_flags.remove(flag)

    def updateFlag(self, flag_id, title, description, location, incident_type):
        for flag in red_flags:
            if flag['id'] == flag_id:
                flag['title'] = title
                flag['description'] = description
                flag['location'] = location
                flag['type'] = incident_type
                return flag


