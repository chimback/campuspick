from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]