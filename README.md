**SOFTWARE ENGINEER PYTHON TEST - REST API**
----

# RESTAPI Documentation

This project was built using Flask where I created a REST endpoint that will return the sum of a list of numbers e.g. [1,2,3] => 1+2+3 = 6

* **URL**

  http://localhost:5000/

## Open Endpoints

Open endpoints require no Authentication.

* [Total](total.md) : `GET /total/`

### Assumptions

Endpoints for viewing and manipulating the Accounts that the Authenticated User
has permissions to access.

* [Show Accessible Accounts](accounts/get.md) : `GET /api/accounts/`
* [Create Account](accounts/post.md) : `POST /api/accounts/`
* [Show An Account](accounts/pk/get.md) : `GET /api/accounts/:pk/`
* [Update An Account](accounts/pk/put.md) : `PUT /api/accounts/:pk/`
* [Delete An Account](accounts/pk/delete.md) : `DELETE /api/accounts/:pk/`