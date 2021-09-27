# Sapid project

## How to setup project?

### Clone the project from Gitlab using HTTPS

```sh
git https://github.com/pratikshatagline/Sapid.git
cd Sapid
```

## create virtual environment
```sh
virtualenv venv
$ source env/bin/activate
```
## freeze requirement.txt
$ pip freeze > requirements. txt

## Then install the dependencies

(env)$ pip install -r requirements.txt

## Run the migrations
(env)$ cd project
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate

## Run the server
(env)$ cd project
(env)$ python manage.py runserver