# Create your views here.
import datetime

import jwt
from rest_framework.response import Response
from rest_framework.views import APIView

from api.auth.my_auth import MyAuthentication


class LoginView(APIView):
    # authentication_classes = [MyAuthentication]

    def post(self, request, *args, **kwargs):
        headers = {
            "alg": "HS256",
            "typ": "JWT"
        }
        # 注意：payload中的 exp 需要用utc时间
        payload = {
            'userid': 1,
            'username': 'abel',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1),  # 过期时间1分钟
        }
        salt = 'secret_key'
        token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers)  # 加密生成字符串

        return Response({
            'code': 1,
            'msg': '登录成功',
            'token': token
        })


class ProfileView(APIView):
    authentication_classes = [MyAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({
            'code': 1,
            'msg': '机密档案',

        })
