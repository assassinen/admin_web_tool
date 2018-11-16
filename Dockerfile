FROM python:3.6-stretch
RUN pip install -U pip

RUN mkdir -p /var/www
WORKDIR /var/www
COPY requirements.txt /var/www
RUN pip install --no-cache-dir -r requirements.txt

CMD python3 server.py
