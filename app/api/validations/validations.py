import re
from werkzeug.security import generate_password_hash
from flask import request


class Validations():
    def get_access_token(self):
        try:
            auth_header = request.headers.get('Authorization')
            access_token = auth_header.split(" ")[1]
            return access_token
        except:
            return None

    def validate_username(self, username):
        if len(username) < 5:
            return False
        else:
            return True

    def validate_email(self, email):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    email):
            return True
        return False

    def validate_incident_type(self, incident):
        inc = str.strip(incident)
        data = inc.lower()
        if data == 'redflag' or data == 'intervention':
            return True
        else:
            return False

    def validate_input_strings(self, string):
        return bool(string and string.strip())

    def validate_password(self, password):
        data = str.strip(password)
        if len(data) == 0:
            return None
        elif len(data) < 5:
            return False
        else:
            return True

    def validate_location(self, location):
        if re.match(r"(^([-+]?\d{1,2}([.]\d+)?),\s*([-+]?\d{1,3}([.]\d+)?)$)",
                    location):
            return True
        return False

    def validate_user_inputs(self, data):
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        username = data['username']
        phone = data['phone']
        raw_pass = data['password']
        valid_email = self.validate_email(email)
        valid_fname = self.validate_input_strings(firstname)
        valid_lname = self.validate_input_strings(lastname)
        valid_username = self.validate_username(username)
        valid_pass = self.validate_password(raw_pass)

        if not valid_email:
            return 'Please enter a valid email'
        elif not valid_fname:
            return'Please enter a valid firstname'
        elif not valid_lname:
            return 'Please enter a valid lastname'
        elif not valid_pass:
            return 'Please enter a valid password'
        elif not valid_username:
            return 'Please enter a valid username. It cannot be less than 5 characters'
        else:
            password = generate_password_hash(raw_pass)
            payload = {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "username": username,
                "phone": phone,
                "password": password
            }
            return payload

    def validate_incident_details(self, data, createdBy):
        title = data['title']
        incident = data['incident']
        location = data['location']
        description = data['description']
        images = data['images']

        valid_title = self.validate_input_strings(title)
        valid_incident = self.validate_incident_type(incident)
        valid_description = self.validate_input_strings(description)
        valid_location = self.validate_location(location)
        if not valid_title:
            return 'Please enter a valid title'
        elif not valid_incident:
            return'Incident should be a redflag or intervention'
        elif not valid_description:
            return 'Please enter a valid description'
        elif not valid_location:
            return 'Please enter a valid location'
        else:
            payload = {
                "title": title,
                "incident": incident,
                "location": location,
                "description": description,
                "images": images,
                "createdBy": createdBy
            }
            return payload
