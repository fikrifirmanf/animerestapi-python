FROM python:slim-buster

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

COPY . /usr/src/app
EXPOSE 8001

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]