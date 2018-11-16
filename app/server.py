#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask

app_test = flask.Flask(__name__)

@app_test.route("/ping")
def ping():
   return "pong"

if __name__ == "__main__":
   app_test.run(host='0.0.0.0')