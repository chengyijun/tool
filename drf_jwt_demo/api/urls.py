# from api.views import LoginView
#
from django.urls import path

from api.views import LoginView, ProfileView

app_name = 'api'
#
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
