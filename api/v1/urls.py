from django.conf.urls import url, include
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^rest-auth/", include("rest_auth.urls")),
    url(r"^profile/", include("api.v1.userprofile.urls")),
]
