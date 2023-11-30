FROM python:3.8-slim-buster

RUN ["mkdir", "-p", "/kafka"]
WORKDIR /kafka


RUN groupadd -r kafka && useradd --no-log-init -r -g kafka kafka

COPY ./kafka/ /kafka/
COPY requirements.txt /kafka/

RUN true \
    && pip install --upgrade pip \
    && pip install --no-cache-dir  -r requirements.txt

USER kafka

# start by default as producer
ENTRYPOINT ["python3", "-m", "kafka"]
CMD ["producer"]