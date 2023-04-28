FROM --platform=arm64 python:3.11

RUN apt-get -y update

WORKDIR /app/mdm2bvh

RUN pip install poetry

COPY /mdm2bvh/pyproject.toml /mdm2bvh/poetry.lock ./

RUN poetry install --no-root

COPY . .