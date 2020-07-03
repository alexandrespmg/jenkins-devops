FROM python:3.7.8-alpine3.12

COPY requirements.txt /tmp/
COPY ./app /app
COPY ./tests /tests
RUN pip install -r /tmp/requirements.txt

RUN python -m unittest