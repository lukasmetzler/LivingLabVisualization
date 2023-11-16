FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y python3

COPY . /app

RUN pip install kafka-python==2.0.2

RUN pip install -r requirements.txt

CMD ["python", "consumer.py"]
