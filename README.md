**SOFTWARE ENGINEER PYTHON TEST - REST API Documentation**
----

This project was built using Flask where I created a REST endpoint that will return the sum of a list of numbers e.g. [1,2,3] => 1+2+3 = 6

## Install and run project
    
    git clone https://github.com/MikeOsa123/DLG_Api.git
    cd DLG_Api
    pip install -r requirements.txt
    export FLASK_APP=api.py
    flask run # run on 127.0.0.1:5000

* **URL**

  http://localhost:5000/

## Open Endpoints

Open endpoints require no Authentication.

* [Total](Total.md) : `GET /total/`

## Run Tests and get Test Coverage
    
    coverage run test_api.py
    coverage report test_api.py


### Assumptions

Endpoints for viewing and manipulating the Accounts that the Authenticated User
has permissions to access.

* [Show Accessible Accounts](accounts/get.md) : `GET /api/accounts/`
* [Create Account](accounts/post.md) : `POST /api/accounts/`
* [Show An Account](accounts/pk/get.md) : `GET /api/accounts/:pk/`
* [Update An Account](accounts/pk/put.md) : `PUT /api/accounts/:pk/`
* [Delete An Account](accounts/pk/delete.md) : `DELETE /api/accounts/:pk/`