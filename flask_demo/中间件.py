# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: demo01.py
@time: 2021/1/12 16:18
@desc:
"""
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)  # 用Api来绑定app


class LoginView(Resource):
    def get(self):
        print('登录了')
        return {'msg': 'login success'}


api.add_resource(LoginView, '/login/', endpoint="login")


@app.route('/')
def index():
    return {'msg': 'Hello World!'}


class MyMiddleware:
    def __init__(self, old_app_wsgi_app):
        self.old_app_wsgi_app = old_app_wsgi_app

    def __call__(self, environ, start_response, *args, **kwargs):
        print('before request')
        res = self.old_app_wsgi_app(environ, start_response)
        print('after request')
        return res


def main():
    app.wsgi_app = MyMiddleware(app.wsgi_app)
    app.run(debug=True)


if __name__ == '__main__':
    main()
