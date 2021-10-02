from django.conf.urls import url
from django.urls import include, path

from .views import AdvisorView

urlpatterns = [
    path("advisor/", AdvisorView.as_view()),
]
