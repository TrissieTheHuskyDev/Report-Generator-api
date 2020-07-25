from django.urls import path, include
from rest_framework import routers
from django.views.generic import TemplateView
from . import views

router = routers.DefaultRouter()
router.register("", views.UserProfileView)
urlpatterns = [path("", include(router.urls))]
