from django.conf.urls import include, url
from rest_framework import routers

from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^auth/", include("rest_auth.urls")),
]
