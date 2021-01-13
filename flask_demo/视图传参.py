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
    def get(self, uid):
        print('登录了')
        print(type(uid), uid)
        return {'msg': 'login success'}


api.add_resource(LoginView, '/login/<int:uid>/', endpoint="login")


@app.route('/test/<int:uid>/')
def index(uid):
    print(type(uid))
    return {'msg': f'Hello World! {uid}'}


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
