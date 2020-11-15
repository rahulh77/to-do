FROM python:3.9-slim AS build

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -y install gcc

COPY requirements.txt .
RUN pip3 install -r ./requirements.txt

FROM python:3.9-slim

COPY --from=build /usr/local/lib/python3.9/site-packages/ \
 /usr/lib/python3.9/.

#  RUN apk --no-cache --update-cache add gcc gcompat

RUN pip3 install gunicorn 

ENV PYTHONPATH "${PYTHONPATH}:/usr/lib/python3.9"

COPY . /app
COPY start.sh /app
WORKDIR /app

ENTRYPOINT ["./start.sh"]