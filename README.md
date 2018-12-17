[![Build Status](https://travis-ci.com/gatemadavid/iReporter2.svg?branch=develop)](https://travis-ci.com/gatemadavid/iReporter2)
[![codecov](https://codecov.io/gh/gatemadavid/iReporter2/branch/develop/graph/badge.svg)](https://codecov.io/gh/gatemadavid/iReporter2) [![Maintainability](https://api.codeclimate.com/v1/badges/096a1db123c0f124022e/maintainability)](https://codeclimate.com/github/gatemadavid/iReporter2/maintainability)
**Project: iReporter**

- iReporter is a platform that allows the public to speak out against corruption and poor development within the society. In case of corruption, users can create a red flag and include the location and description of the incident so that the relevant agencies can investigate. On the other hand, users can seek government intervention in areas such as poor infrastructure.

**Getting Started**

This is a python3 project and users will require an environment that runs python 3 before cloning the repo.

**Prerequisites**

```

- [Python3](https://www.python.org/download/releases/3.0/)
- [Flask](http://flask.pocoo.org/)
- [Flask RESTFul](https://flask-restful.readthedocs.io/en/latest/)

```

**Installing**
Create a python3 virtual environment using:

```
- virtualenv -p python3 env

```

**Activate the virtual environment using:**

```
- source env/bin/activate
```

**Clone the Repository**

```
- git clone https://github.com/gatemadavid/iReporter2.git

```

**Install Dependencies**

```
- pip install -r requirements.txt
```

**Export the environment variable**

```
- export FLASK_APP=run.py
```

**Run Application**

```
- flask run
```

**Test Endpoints**

```
- Testing the api endpoints should be done on [Postman](https://www.getpostman.com/)
```

**Post a red flag**

- POST /api/v2/users
  ![reg](https://user-images.githubusercontent.com/27230922/50077780-659ecf80-01f6-11e9-9420-99c12c7dc859.png)

**Login user**

- POST /api/v2/login
  ![login](https://user-images.githubusercontent.com/27230922/50078045-fd042280-01f6-11e9-8aef-4ab48c96ad68.png)

**Create Incident**

- POST /api/v2/incidents
  ![incident](https://user-images.githubusercontent.com/27230922/50078120-2e7cee00-01f7-11e9-915c-b5f74da784eb.png)

The id field is added and incremented automattically

**Fetch all Incidents**

- GET /api/v2/incidents
  ![all inc](https://user-images.githubusercontent.com/27230922/50078278-9cc1b080-01f7-11e9-972b-bb193864d522.png)

**Fetch one Incident**

- GET /api/v2/incidents/<id>
  ![one incident](https://user-images.githubusercontent.com/27230922/50078193-6421d700-01f7-11e9-8421-821ef12db27b.png)

**Delete an Incident**

- DELETE /api/v2/incidents/<id>

![delete](https://user-images.githubusercontent.com/27230922/50078332-bbc04280-01f7-11e9-8a7c-b57e207775b9.png)

**Update Incident**

- PUT /api/v2/incidents/<id>
  ![put]![update inc](https://user-images.githubusercontent.com/27230922/50078396-eca07780-01f7-11e9-8e30-e90202cde035.png)

**Update User**
PUT /api/v2/users<id>
![edit user](https://user-images.githubusercontent.com/27230922/50078573-69cbec80-01f8-11e9-8b9e-5a44543b0da6.png)

**Alternative API Consumption**
The application is hosted on heroku and it can be accessed via postman on the following link:

- https://ireporter2-heroku.herokuapp.com/api/v1/redflags

**Running Tests**

- pytest

**Authors**

- David Muriithi Gatema

**License**

- This project is licensed under the MIT License
