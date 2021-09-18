FROM python:3.8-slim-buster
RUN apt-get update --fix-missing
RUN apt-get install -y libgl1-mesa-dev python3-pip git

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -U setuptools
RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app
WORKDIR /app
RUN ls
ENTRYPOINT gunicorn --bind :8080 --workers 2 --threads 8 main:app --worker-class uvicorn.workers.UvicornH11Worker --preload --timeout 60 --worker-tmp-dir /dev/shm

