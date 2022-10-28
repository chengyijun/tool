import datetime

import jwt
"""
pip install pyjwt
"""


def encode():
    """
    jwt (json web token) 加密字符串由三段组成并通过点号分割
    第一段：由固定格式的header通过 base64url加密而成
    第二段：由payload通过 base64url 加密而成
    第三段：校验段 由第一段.第二段 加密后的字符串  加盐并进行HS256加密  之后再对产生的结果进行 base64url加密 产生
    :return:
    """
    headers = {"alg": "HS256", "typ": "JWT"}
    # 注意：payload中的 exp 需要用utc时间
    payload = {
        'userid': 1,
        'username': 'abel',
        'exp':
        datetime.datetime.utcnow() + datetime.timedelta(seconds=1),  # 过期时间
    }
    salt = 'secret_key'
    s = jwt.encode(payload=payload,
                   key=salt,
                   algorithm='HS256',
                   headers=headers)  # 加密生成字符串
    print(s)
    return s


def decode(s):
    salt = 'secret_key'
    s = jwt.decode(s, key=salt, algorithms=['HS256'])  # 解密，校验签名
    print(s)
    print(type(s))


# jwt.exceptions.DecodeError
# jwt.exceptions.ExpiredSignatureError
# jwt.exceptions.DecodeError:


def main():
    s = encode()
    decode(s)


if __name__ == '__main__':
    main()
