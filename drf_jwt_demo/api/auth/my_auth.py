import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        salt = 'secret_key'
        headers = {
            "alg": "HS256",
            "typ": "JWT"
        }
        token = request.query_params.get('token')

        try:
            payload = jwt.decode(token, key=salt, algorithms=['HS256'], headers=headers)  # 解密，校验签名
        except jwt.exceptions.ExpiredSignatureError:
            raise AuthenticationFailed(detail={'msg': 'token过期了'})
        except Exception:
            raise AuthenticationFailed(detail={'msg': '认证失败'})
        # jwt.exceptions.DecodeError
        # jwt.exceptions.ExpiredSignatureError
        # jwt.exceptions.DecodeError:
        print(payload)
        return payload, token
