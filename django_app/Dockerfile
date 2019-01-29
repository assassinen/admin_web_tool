FROM python:3.6-stretch
RUN pip install -U pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

#CMD FLASK_APP=run.py FLASK_DEBUG=1 flask run
CMD ["python", "manage.py", "runserver", "8000"]