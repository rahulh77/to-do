#!/bin/sh
# export PYTHONUNBUFFERED=TRUE
rm -rf ./*.db
rm -rf ./tmp
mkdir -p `pwd`/tmp
export prometheus_multiproc_dir=`pwd`/tmp
gunicorn --chdir app \
    run-app:app \
    -c gunicorn_config.py \
    -w 3 --threads 4 \
    --log-level=DEBUG \
    -b 0.0.0.0:5000