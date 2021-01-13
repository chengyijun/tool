# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: demo01.py
@time: 2021/1/12 16:18
@desc:
"""
from flask import Flask, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)  # 用Api来绑定app


@app.route('/login', methods=['POST'])
def login():
    print(request.data.decode('utf-8'))
    return {'msg': 'login!'}


@app.route('/')
def index():
    return {'msg': 'index!'}


@app.route('/about')
def about():
    return {'msg': 'about!'}


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
