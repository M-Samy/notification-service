FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
COPY ./app/compose/requirements.txt /requirements.pip
RUN pip3.6 install -r /requirements.pip

COPY ./app/compose/uvicorn.sh /uvicorn.sh
COPY ./app /service

WORKDIR /service
RUN chmod +x ./compose/uvicorn.sh
ENTRYPOINT ["sh", "./compose/uvicorn.sh"]
