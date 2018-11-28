FROM python:3.6-stretch
RUN pip install -U pip

RUN mkdir -p /app/flask-jwt
WORKDIR /app/flask-jwt
COPY requirements.txt /app/flask-jwt
RUN pip install --no-cache-dir -r requirements.txt

#CMD FLASK_APP=run.py FLASK_DEBUG=1 flask run
CMD FLASK_APP=run.py FLASK_DEBUG=1 flask run --host=0.0.0.0 --port=5000