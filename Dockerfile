FROM python:3.7.4

WORKDIR /django
COPY . /django/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
