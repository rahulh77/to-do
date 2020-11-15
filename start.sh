#!/bin/sh
# export PYTHONUNBUFFERED=TRUE
rm -rf ./*.db
gunicorn --chdir app run-app:app -w 3 --threads 4 --log-level=DEBUG -b 0.0.0.0:5000