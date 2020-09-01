# Total

Used to collect a Token for a registered User.

**URL** : `/api/login/`

**Method** : `GET`

**Auth required** : NO

**Data example**

```json
{
    "total": 50005000
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "token": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d"
}
```

## Error Response

**Condition** : If list provided in the backend is empty

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "non_field_errors": [
        "List provided is empty"
    ]
}
```