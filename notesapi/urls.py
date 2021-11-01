from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, UserViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet, basename="articles")
router.register(r"", UserViewSet)

app_name = "notes"

urlpatterns = [
    path("", include(router.urls)),
]
