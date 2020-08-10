from django.conf.urls import url, include
from rest_framework import routers
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^", include("api.v1.userprofile.urls")),
    url(r"^rest-auth/", include("rest_auth.urls")),
    # url(r"^rest-auth/del-token", ),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
