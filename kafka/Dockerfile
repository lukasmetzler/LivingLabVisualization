FROM python:3.11

WORKDIR /app

# Install dependencies for Kafka
RUN apt-get update && apt-get install -y default-jre

# Copy requirements.txt
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install kafka-python==2.0.2
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "consumer.py"]
