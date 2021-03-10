from django.urls import path

from demo.views import LoginView, path1, path2, path3

app_name = 'demo'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('path1/', path1, name='path1'),
    path('path2/', path2, name='path2'),
    path('path3/', path3, name='path3'),
]
