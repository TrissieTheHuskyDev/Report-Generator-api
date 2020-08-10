from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from django.views.generic import TemplateView
from .views import ProfileDetailView, ProfileView


router = routers.DefaultRouter()
router.register("", ProfileView)


urlpatterns = [
    url(r'^profile/$',ProfileDetailView.as_view(), name='user_profile' ),
    path("", include(router.urls))
]

