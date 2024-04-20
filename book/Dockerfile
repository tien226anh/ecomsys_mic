FROM python:3.11

RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/

RUN python manage.py migrate
RUN python manage.py migrate --database=book_mongo

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
