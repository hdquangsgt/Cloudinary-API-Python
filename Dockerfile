FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY main.py .

ENV FLASK_APP=main.py

EXPOSE 5000

CMD python main.py

