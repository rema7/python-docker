# Microservice with python
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