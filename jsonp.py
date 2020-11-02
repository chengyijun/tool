# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: jsonp.py
@time: 2020/11/2 8:55
@desc:
"""
import json

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def test():
    try:
        callback_fun = request.query_string.decode('utf-8').split('=')[1]
    except:
        return '请求url必须包含query参数'
    data = {
        'code': 1,
        'msg': '你好啊 小八'
    }
    # return f'{callback_fun}({json.dumps(data, ensure_ascii=False)})'

    # 2 使用make_response 来构造响应信息
    resp = make_response(f'{callback_fun}({json.dumps(data, ensure_ascii=False)})')  # 响应体
    # 设置响应头
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Content-Type"] = "application/json"
    return resp


def main():
    app.run()


if __name__ == '__main__':
    main()
