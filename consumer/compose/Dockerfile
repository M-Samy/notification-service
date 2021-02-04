FROM python:3.6-slim as base

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
COPY ./consumer/compose/requirements.txt /requirements.pip
RUN pip3.6 install -r /requirements.pip

FROM base

COPY ./consumer /worker
COPY ./consumer/server.py /worker

WORKDIR /worker
ENTRYPOINT ["python3", "server.py"]
