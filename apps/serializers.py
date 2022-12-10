from rest_framework.serializers import ModelSerializer

from apps.models import Region, Category


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
