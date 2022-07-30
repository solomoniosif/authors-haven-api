from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Authors API",
        default_version="v1",
        description="API endpoints for the Authors API course",
        contact=openapi.Contact(email="solomoniosif@gmail.com"),
        licence=openapi.License(name="MIT Licence", )
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc"
    ),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/articles/", include("core_apps.articles.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
    path("api/v1/comments/", include("core_apps.comments.urls")),
]

admin.site.site_header = "Authors Haven API Admin"
admin.site.site_title = "Authors Haven API Admin Portal"
admin.site.index_title = "Welcome to the Authors Haven API Portal"
