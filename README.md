# Microservice with python v1.0
This is just a simple python web service comprised only one REST method.

## Quickstart via docker
```
$ cd ./docker
$ docker-compose up
```

## Quickstart from scratch
```bash
$ mkvirtualenv python-falcon-microservice -p python3.6
$ pip install -r ./src/.meta/packages
$ cd ./src
$ gunicorn app:app -c gunicorn.conf.py --reload

```