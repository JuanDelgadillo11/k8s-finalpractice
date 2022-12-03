FROM python:3.10.8-slim-bullseye
WORKDIR /

COPY requirements.txt requirements.txt
RUN apt-get update  && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000

ARG MYSQL_HOST
ENV MYSQL_HOST=127.0.0.1
RUN echo $MYSQL_HOST

ARG MYSQL_PORT
ENV MYSQL_PORT=3306
RUN echo $MYSQL_PORT

ENV FLASK_APP=main.py
CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]