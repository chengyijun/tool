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


def auth(fun):
    def inner(*args, **kwargs):
        print('执行试图函数之前 执行权限认证')
        res = fun(*args, **kwargs)
        print('执行试图函数之后 进行后续操作')
        return res

    return inner


class LoginView(Resource):
    method_decorators = [auth]

    def get(self):
        print('登录了')
        return {'msg': 'login success'}


def main():
    # 创建蓝图
    _api = Blueprint('api', __name__)

    api = Api(_api)
    # 设置路由
    api.add_resource(LoginView, '/login', endpoint="login")

    # 注册蓝图
    app = Flask(__name__)
    app.register_blueprint(_api, url_prefix='/api')
    app.run(debug=True)


if __name__ == '__main__':
    main()
