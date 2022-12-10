from rest_framework.viewsets import ModelViewSet

from apps.models import Region, Category
from apps.serializers import RegionModelSerializer, CategoryModelSerializer


class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
