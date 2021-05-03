from django.urls import include,path
from django.conf.urls import url
from .api import RegisterApi

urlpatterns = [
    path('register/', RegisterApi.as_view()),
]
