[![Build Status](https://travis-ci.com/gatemadavid/iReporter2.svg?branch=develop)](https://travis-ci.com/gatemadavid/iReporter2)
[![Coverage Status](https://coveralls.io/repos/github/gatemadavid/iReporter2/badge.svg?branch=develop)](https://coveralls.io/github/gatemadavid/iReporter2?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/096a1db123c0f124022e/maintainability)](https://codeclimate.com/github/gatemadavid/iReporter2/maintainability)
**Project: iReporter**

```
- iReporter is a platform that allows the public to speak out against corruption and poor development within the society. In case of corruption, users can create a red flag and include the location and description of the incident so that the relevant agencies can investigate. On the other hand, users can seek government intervention in areas such as poor infrastructure.
```

**Getting Started**

```
This is a python3 project and users will require an environment that runs python 3 before cloning the repo.
```

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

- POST /api/vi/redflags

_Expected Data format:_

{
"title":"Bad Road",

"description": "Potholes on the road",

"location":"Ronald Ngars Street",

"type":"Intervention"

}

![post](https://user-images.githubusercontent.com/27230922/49425507-e00b3080-f7ae-11e8-8cb1-be9755b7c143.png)

The id field is added and incremented automattically

**Fetch all Redflags**

```
- GET /api/v1/redflgas
```

![get all](https://user-images.githubusercontent.com/27230922/49426053-65431500-f7b0-11e8-92c2-1ff211e8fc31.png)

**Fetch one Redflag**

```
- GET /api/vi/redflags/<id>
```

![get one](https://user-images.githubusercontent.com/27230922/49426088-83107a00-f7b0-11e8-95f1-63b8384de316.png)

**Delete a Redflag**

```
- DELETE /api/v1/redflags/<id>
```

![delete](https://user-images.githubusercontent.com/27230922/49426392-80625480-f7b1-11e8-81a6-a1ede1453818.png)

**Update Red flag**

```
- PUT /api/vi/redflgas/<id>
```

![put](https://user-images.githubusercontent.com/27230922/49426254-16e24600-f7b1-11e8-9a02-b209da3ce7ed.png)

**Alternative API Consumption**
The application is hosted on heroku and it can be accessed via postman on the following link:

- https://ireporter2-heroku.herokuapp.com/api/v1/redflags

**Running Tests**

```
- pytest
```

**Authors**

```
- David Muriithi Gatema
```

**License**

```
- This project is licensed under the MIT License
```
