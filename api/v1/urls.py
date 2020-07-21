from django.conf.urls import url, include
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^profile/", include("api.v1.profile.urls")),
    url(r"^announcements/", include("api.v1.announcements.urls")),
    url(r"^documents/", include("api.v1.documents.urls")),
    url(r"^chat/", include("api.v1.chat.urls")),
    url(r"^rest-auth/", include("api.v1.rest_auth.urls")),
    url(r"^rest-auth/registration/", include("api.v1.rest_auth.registration.urls")),
]
