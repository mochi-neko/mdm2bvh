FROM --platform=arm64 python:3.10

RUN apt-get -y update

WORKDIR /app/mdm2bvh

RUN pip install poetry

COPY /mdm2bvh/pyproject.toml ./
COPY /mdm2bvh/poetry.lock ./
COPY /mdm2bvh/src ./
COPY /mdm2bvh/README.md ./

RUN poetry install

COPY . .