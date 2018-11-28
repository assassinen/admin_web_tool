#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, abort, Flask, jsonify, make_response


app = Flask(__name__)

tasks = [{'id': 1}]

@app.route('/')
def send_static():
    return 'pong'

#{POST /auth/register} (in: json{data: {parther_id:int, client_id:int, cashbox_id:int}}; out:jwt)
@app.route('/auth/register', methods=['POST'])
def register():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/auth/register', methods=['GET'])
def get_tasks():
    return jsonify({'message': 'Hello, World!'})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
