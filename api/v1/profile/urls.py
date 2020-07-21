from django.conf.urls import url

from rest_auth.views import LoginView

urlpatterns = [
    url(r"^", LoginView.as_view(), name="rest_login"),
]
