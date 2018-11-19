#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import json
import os

DATAFILE="data.txt"
ROOT='/var/www'

app_test = flask.Flask(__name__, static_folder=ROOT)

@app_test.route('/')
@app_test.route('/<path:path>')
def send_static(path = False):
    # Здесь мы посылаем всю статику клиенту - html, js скрипты, css стили
    print('Requested file path: {0}'.format(path))

    if not path:
        return app_test.send_static_file('index.html')

    return app_test.send_static_file(path)


@app_test.route("/server/list")
def list():
   # Читаем построчно информацию из файла, и добавляем в список (dict_list)
   with open("data.txt", "r") as file_descriptor:
       try:
           data = file_descriptor.read()
           file_descriptor.close()
       except Exception:
           return "false"
   return data

@app_test.route("/server/add")
def add():
    print("Recevied args: {0}".format(flask.request.args))
    message_dict = flask.request.args.to_dict()
    print("Message dict: {0}".format(message_dict))
    with open("data.txt", "a+") as file_descriptor:
        try:
            element = json.dumps(message_dict)
            print("Element will be writed in file: {0}".format(element))
            file_descriptor.write(element)
            file_descriptor.write('\n')
            file_descriptor.close()
        except Exception as e:
            return "false"
    return "true"

if __name__ == "__main__":
    app_test.run(host='0.0.0.0', port=5000, debug=True)
