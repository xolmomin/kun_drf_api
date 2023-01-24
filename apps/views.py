from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, NOT
from rest_framework.viewsets import ModelViewSet

from apps.documents import BlogDocument
from apps.models import Region, Category, Blog
from apps.serializers import RegionModelSerializer, CategoryModelSerializer, BlogModelSerializer, BlogDocumentSerializer


class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    filter_backends = (DjangoFilterBackend,)
    parser_classes = (MultiPartParser, )
    filterset_fields = ('name',)
    # permission_classes = (~IsAuthenticated, )
    # permission_classes = (NOT(IsAuthenticated), )
    # search_fields = ('name', )


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class BlogDocumentViewSet(DocumentViewSet):
    document = BlogDocument
    filter_backends = [SearchFilterBackend]
    serializer_class = BlogDocumentSerializer
    search_fields = ('title', 'text')