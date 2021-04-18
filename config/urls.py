from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import  IsAdminUser

docs_view = include_docs_urls(
    title = 'drf API',
    description='API document',
    permission_classes=[IsAdminUser]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', docs_view),
    path('board/', include('board.urls')),
    path('user/', include('user.urls')),
]
