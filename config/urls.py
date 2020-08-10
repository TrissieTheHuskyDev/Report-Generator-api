from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # DEFAULT API DOCS HOMEPAGE
    url(r"^", include_docs_urls(title="API")),
    # ADMIN URL ENDPOINT
    url(r"^admin/", admin.site.urls),
    # API URL ENDPOINT
    url(r"^api/v1/", include("api.v1.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

