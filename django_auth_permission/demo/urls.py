from demo.views import LoginView
from demo.views import RegisterView
from django.urls import path

app_name = 'demo'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
