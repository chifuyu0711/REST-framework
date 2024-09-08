from rest_framework import viewsets
from .serializers import AuthorModelSerializer, BookModelSerializer, CategoryModelSerializer
from .models import Author, Book, Category


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelSerializerViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class CategoryModelSerializerViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
