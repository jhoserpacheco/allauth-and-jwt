# SMALL APP OAUTH WITH GOOGLE 
<hr>

## INSTALLATION

### Clone repository use

``git clone https://github.com/Sachica/allauth-and-jwt``

#### Change directory and Activate Environment
``cd allauth-and-jwt``
``python -m venv env``
``. env/bin/activate``

#### Install requirements.txt and make migrations 
``pip install -r requirements.txt``
``python manage.py makemigrations``
``python manage.py migrate``

#### Run server 
``python manage.py runserver``

<hr>

## VARIABLES ENVIRONMENTS 

#### Create file '.env' with:
* CLIENTE_ID=ID_CLIENT_GOOGLE_API
* SECRET=SECRET_CLIENT_GOOGLE_API
* SECRET_KEY=DJANGO_SECRET_KEY 

<hr>

## POSTMAN 
* Sign in with google on: http://127.0.0.1:8000/accounts/google/login
* Get access_token http://127.0.0.1:8000/user/get-token/  

```yaml
Response
{
    "refresh": "REFRESH_TOKEN",
    "access": "ACCESS_TOKEN"
}
```
* View Profile http://127.0.0.1:8000/user/profile/

```yaml 
Response
{
    "id": 1,
    "last_login": "2022-04-14T15:32:27.740858Z",
    "is_superuser": false,
    "username": "user_example",
    "first_name": "example1",
    "last_name": "example2",
    "email": "example@example.com",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2022-04-14T14:30:09.693939Z",
    "groups": [],
    "user_permissions": []
}
```

* Verify token_access http://127.0.0.1:8000/user/api/token/verify/
    *  'token' : 'token_access'

<hr>
