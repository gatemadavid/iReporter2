[![Build Status](https://travis-ci.com/gatemadavid/iReporter2.svg?branch=develop)](https://travis-ci.com/gatemadavid/iReporter2) [![codecov](https://codecov.io/gh/gatemadavid/iReporter2/branch/develop/graph/badge.svg)](https://codecov.io/gh/gatemadavid/iReporter2)

**Project: iReporter**

- iReporter is a platform that allows the public to speak out against corruption and poor development within the society. In case of corruption, users can create a red flag and include the location and description of the incident so that the relevant agencies can investigate. On the other hand, users can seek government intervention in areas such as poor infrastructure.

**Getting Started**
This is a python3 project and users will require an environment that runs python 3 before cloning the repo.

**Prerequisites**

- [Python3](https://www.python.org/download/releases/3.0/)
- [Flask](http://flask.pocoo.org/)
- [Flask RESTFul](https://flask-restful.readthedocs.io/en/latest/)

**Installing**
Create a python3 virtual environment using:

- virtualenv -p python3 env

**Activate the virtual environment using:**

- source env/bin/activate

**Clone the Repository**

- git clone https://github.com/gatemadavid/iReporter2.git

**Install Dependencies**

- pip install -r requirements.txt

**Export the environment variable**

- export FLASK_APP=run.py

**Run Application**

- flask run

**Test Endpoints**

- Testing the api endpoints should be dome on [Postman](https://www.getpostman.com/)

  **Post a red flag**

- POST /api/vi/redflags

_data should be json formatted_
{
"title": title,
"description": description,
"location": location,
"type": incident_type
}

The id field is added and incremented automattically

**Fetch all Redflags**

- GET /api/v1/redflgas

**Fetch one Redflag**

- GET /api/vi/redflags/<id>

**Delete a Redflag**

- DELETE /api/v1/redflags/<id>

**Update Red flag**

- PUT /api/vi/redflgas/<id>

**Alternative API Consumption**
The application is hosted on heroku and it can be accessed via postman on the following link:

- https://ireporter2-heroku.herokuapp.com/api/v1/redflags

**Running Tests**

- pytest

**Authors**

- David Muriithi Gatema

**License**

- This project is licensed under the MIT License
