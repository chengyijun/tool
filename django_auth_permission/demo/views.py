# Create your views here.

# some_view.py
import json

from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Permission
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views import View


class RegisterView(View):
    def post(self, request: WSGIRequest):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        print(data)
        username = data.get('username')
        password = data.get('password')
        # 由于django自带认证里面 登录密码是加密的 此处需要使用django提供的密码加密函数
        password = make_password(password)

        # Django自带的认证中  注册一个用户  用户名 密码 邮箱 三项是必须的 其他的是可选的
        user = User(username=username, password=password, email=f'{username}@gmail.com')
        user.save()
        return JsonResponse({
            'code': 1,
            'message': f'{username} 注册成功!'
        })


class LoginView(View):
    def post(self, request: WSGIRequest):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        print(data)
        username = data.get('username')
        password = data.get('password')

        # Django提供的authenticate函数，验证用户名和密码是否在数据库中匹配
        # 其实就是通过User()模型来查询是否存在该用户名和密码的用户，如果有就返回该用户对象，没有就返回None
        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            return JsonResponse({
                'code': 0,
                'message': f'{username} 登录失败！'
            })
        # Django提供的login函数，将当前登录用户信息保存到会话key中
        login(request, user)
        # 保存的session信息可以查看
        # pprint(request.session.__dict__)
        # 判断用户是否登录
        print(request.user.is_authenticated, '000000000000000')

        # 设置权限
        perm1 = Permission.objects.first()
        user.user_permissions.add(perm1)
        print(perm1.__dict__)
        print(perm1, perm1.name)
        print(user.get_user_permissions())
        print(user.get_all_permissions())
        # has_perm('app_name'.'codename')
        print(user.has_perm('admin.add_logentry'), '==========')
        # print(user.has_perm(user.get_user_permissions()), '************')
        # 自定义权限
        # content_type = ContentType.objects.get_for_model(BlogPost)
        # perm2 = Permission.objects.create(codename='can_publish',
        #                                   name='Can Publish Posts',
        #                                   content_type=content_type)
        # user.user_permissions.add(perm2)
        print(user.get_user_permissions())
        print(user.has_perm('demo.can_publish'), '==========')
        return JsonResponse({
            'code': 1,
            'message': f'{username} 登录成功！'
        })
