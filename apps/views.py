from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from apps.models import Region, Category
from apps.serializers import RegionModelSerializer, CategoryModelSerializer


class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', )
    # search_fields = ('name', )


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
