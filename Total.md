# Total

Total endpoint that takes a list from the backend and sums up the numbers in that list.

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