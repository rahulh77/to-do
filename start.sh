#!/bin/sh
rm -rf ./*.db
gunicorn --chdir app run-app:app -w 2 --threads 2 --log-level=DEBUG -b 0.0.0.0:5000