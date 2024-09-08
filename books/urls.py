from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import AuthorModelViewSet, BookModelSerializerViewSet, CategoryModelSerializerViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelViewSet)

router.register(r'books', BookModelSerializerViewSet)

router.register(r'category', CategoryModelSerializerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]