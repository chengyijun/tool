from api.views import TestView
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('test/', TestView.as_view(), name='test')
]
