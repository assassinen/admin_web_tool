#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import json

app_test = flask.Flask(__name__)
DATAFILE = "data.txt"


@app_test.route("/ping")
def ping():
    return "pong"


@app_test.route("/add")
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


@app_test.route("/get")
def get():
    message_dict = flask.request.args.to_dict()
    user_id = flask.request.args.to_dict()['user_id']

    with open("data.txt", "r") as file_descriptor:
        try:
            for string in file_descriptor:
                element = json.loads(string)
                if element['user_id'] == user_id:
                    return json.dumps(element)
        except Exception:
            return "false"
    return "false"


@app_test.route("/remove")
def remove():
    user_id = flask.request.args.to_dict()['user_id']
    dict_list = []

    # Читаем построчно информацию из файла, и добавляем в список (dict_list)
    with open("data.txt", "r") as file_descriptor:
        try:
            for string in file_descriptor:
                element = json.loads(string)
                dict_list.append(element)
            file_descriptor.close()
        except Exception:
            return "false"

    # Удаляем все из файла ("w" в в функции open() -
    # значит предварительно удалить все содержимое),
    # пишем в файл все что у нас есть в dict_list,
    # кроме элемента у которого user_id равен тому,
    # который мы получили из аргументов метода /remove

    with open("data.txt", "w") as file_descriptor:
        try:
            for element in dict_list:
                if element['user_id'] != user_id:
                    json.dump(element, file_descriptor)
                    # каждый элемент пишем на новую строку
                    file_descriptor.write('\n')
            file_descriptor.close()

        except Exception:
            return "false"

    return "true"


@app_test.route("/server/list")
def list():
    # Читаем построчно информацию из файла возвращаем весь
    with open(DATAFILE, "r") as file_descriptor:
        try:
            data = file_descriptor.read()
            file_descriptor.close()
        except Exception:
            return "false"
    return data


if __name__ == "__main__":
    app_test.run(host='0.0.0.0', port=5000)
