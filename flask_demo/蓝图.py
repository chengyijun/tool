# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: demo01.py
@time: 2021/1/12 16:18
@desc:
"""
from flask import Blueprint, Flask
from flask_restful import Api, Resource

# 创建蓝图
_api = Blueprint('api', __name__)

api = Api(_api)


class LoginView(Resource):
    def get(self):
        print('登录了')
        return {'msg': 'login success'}


# 设置url
api.add_resource(LoginView, '/login', endpoint="login")

# 注册蓝图
app = Flask(__name__)
app.register_blueprint(_api, url_prefix='/api')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
