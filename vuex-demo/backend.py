# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: backend.py
@time: 2021/3/9 10:38
@desc:
"""
import json
import uuid
from pprint import pprint

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/login/', methods=['POST'])
def test():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    print(data)
    token = uuid.uuid4().hex
    return jsonify({'code': 1, 'mesage': '登录成功！', 'username': data.get('username'), 'token': token})


@app.route('/api/profile/')
def profile():
    pprint(request.headers.__dict__.get('environ').get('HTTP_AUTHORIZATION'))
    return jsonify({'code': 1, 'mesage': '机密档案~~~！'})


def main():
    app.run()


if __name__ == '__main__':
    main()
