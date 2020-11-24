#!/bin/sh
# export PYTHONUNBUFFERED=TRUE
# https://stackoverflow.com/questions/10855197/gunicorn-worker-timeout-error
rm -rf ./*.db
rm -rf ./tmp
mkdir -p `pwd`/tmp
export prometheus_multiproc_dir=`pwd`/tmp
gunicorn --chdir app \
    run-app:app \
    -c gunicorn_config.py \
    -w 1 \
    --log-level=DEBUG \
    --timeout 90 \
    -b 0.0.0.0:5000