from django.urls import include,path
from django.conf.urls import url
from .views import UserView


urlpatterns = [
    path('register/', UserView.as_view()),
]
