# -*- coding: utf-8 -*-

from run import app
from flask import jsonify

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})