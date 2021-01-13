# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: demo01.py
@time: 2021/1/12 16:18
@desc:
"""
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
# 解决跨域
CORS(app, supports_credentials=True)

api = Api(app)


class LoginView(Resource):
    def get(self, uid):
        print('登录了')
        print(type(uid), uid)
        return {'msg': 'login success'}


# 设置url
api.add_resource(LoginView, '/login/<int:uid>/', endpoint="login")


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
