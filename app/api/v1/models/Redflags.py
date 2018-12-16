
red_flags = []


class RedFlagsModel():
    def __init__(self):
        self.db = red_flags

    def save(self, data):
        id = len(red_flags) + 1
        payload = {
            "id": id,
            "title": data['title'],
            "description":  data['description'],
            "location": data['location'],
            "type": data['type']
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

    def updateFlag(self, flag_id, data):
        for flag in red_flags:
            if flag['id'] == flag_id:
                flag['title'] = data['title']
                flag['description'] = data['description']
                flag['location'] = data['location']
                flag['type'] = data['type']
                return flag
