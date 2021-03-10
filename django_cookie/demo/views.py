from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):
    def get(self, request: WSGIRequest):
        # session 在django里面非常简单  直接通过request对象调用像字典一样存储 读取就行了
        # 设置session的内部过程
        #   1.生成随机字符串
        #   2.将随机字符串通过set_cookie交给浏览器 同时服务器端保存一份到 django_session数据库表中 内容加密
        # 浏览器中的cookie---->
        #   {'sessionid': 'v0n75erkjshqu8jui6xekrrn4zo2i28n'}
        # django_session数据表中---->
        #     {'session_key': 'v0n75erkjshqu8jui6xekrrn4zo2i28n',
        #       'session_data': 'eyJra2siOiJ4eHh4eHgifQ:1lJrnI:vuT9gTmCygf0JRbx-QihJ9EOPA_lA9rIJE1ThXegBCo'
        #     }
        #   3.校验的时候 通过浏览器传递过来的cookie（保存的是sessionid） 服务器在数据表中查询 有就去除并解密
        request.session['kkk'] = 'xxxxxx'
        print(request.session['kkk'])
        return render(request, 'login.html')

    def post(self, request: WSGIRequest):
        print(request.POST.dict())
        obj = render(request, 'login.html')
        # obj是响应  给响应头设置cookie
        # render() redirect() HttpResponse() 返回值都是Response对象 都可以设置cookie
        # 可以设置过期时间 max_age 单位是秒
        obj.set_cookie('name', 'abel----111------', max_age=20)
        return obj


def path1(request: WSGIRequest):
    print('path1-----', request.COOKIES)
    obj = HttpResponse('path1')
    # path='/demo/path1/' 表示 这个cookie 只在这个 url 下生效 其他url获取不到该cookie
    # 默认path='/' 表示该cookie在所有url页面下均有效
    obj.set_cookie('k8888888', 'v888888', path='/demo/path1/')
    return obj


def path2(request: WSGIRequest):
    print(request.COOKIES)
    obj = HttpResponse('path2')

    return obj


def path3(request: WSGIRequest):
    if request.COOKIES.get('k8888888') is not None:
        print('path3-----', request.get_signed_cookie('k8888888', salt='abel'))
    obj = HttpResponse('path3')
    # 通过 salt='abel' 指定盐 给cookie的值进行加密
    # 浏览器端获得的cookie值 'v888888:1lJpRK:srYVQNBjULnOXvBXLbWgu7QrK0M_OJ0VAwJapZTpOdI'
    obj.set_signed_cookie('k8888888', 'v888888', salt='abel')
    return obj


from django.core.signing import TimestampSigner


class MySigner(TimestampSigner):
    """
    重写cookie加密解密方法
    """

    def sign(self, value):
        return value + 'xxxxooxx'

    def unsign(self, signed_value, max_age=None):
        return signed_value[0:-8]
