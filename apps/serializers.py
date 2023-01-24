from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework.serializers import ModelSerializer

from apps.documents import BlogDocument
from apps.models import Region, Category, Blog


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BlogDocument
        fields = [
            'id',
            'title',
            'text'
        ]
