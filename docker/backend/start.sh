#!/bin/bash

service ssh start

pip install --pre -U -r /app/src/.meta/packages

gunicorn app:app -c gunicorn.conf.py --reload
