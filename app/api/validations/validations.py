import re


class Validations():
    def validate_username(self, username):
        if len(username) < 7:
            return False
        elif re.match("^[a-zA-Z0-9_-]+$", username):
            return True
        else:
            return False

    def validate_email(self, email):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    email):
            return True
        else:
            return False

    def validate_incident_type(self, incident):
        inc = str.strip(incident)
        data = inc.lower()
        if data != 'redflag' or data != 'intervention':
            return False
        else:
            return True

    def validate_input_strings(self, string):
        return bool(string and string.strip())

    def validate_password(self, password):
        data = str.strip(password)
        if len(data) == 0:
            return None
        elif len(data) < 7:
            return False
        else:
            return True
