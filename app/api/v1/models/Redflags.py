
red_flags = []


class RedFlagsModel():
    def __init__(self):
        self.db = red_flags

    def save(self, data):
        id = len(red_flags) + 1
        payload = {
            "id": id,
            "title": data["title"],
            "description": data["description"],
            "location": data["location"],
            "incident_type": data["incident_type"],
            "images": data["images"]
        }
        self.db.append(payload)
        return self.db

    def get_flags(self):
        return self.db

    def get_single_flag(self, flag_id):
        for flag in red_flags:
            if flag['id'] == flag_id:
                return flag

    def delete_flag(self, flag_id):
        for flag in red_flags:
            if flag['id'] == flag_id:
                return red_flags.remove(flag)

    def update_flag(self, flag_id, description, location):
        for flag in red_flags:
            if flag['id'] == flag_id and flag['status'] == 'new':
                flag['description'] = description
                flag['location'] = location
                return flag
