FROM python:3.8-slim-buster

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9001

CMD ["python","manage.py", "runserver", "127.0.0.1:9001"]