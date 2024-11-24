FROM python:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends git\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD bash start
