from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import RegionModelViewSet, CategoryModelViewSet, BlogModelViewSet, BlogDocumentViewSet

router = DefaultRouter()
router.register('region', RegionModelViewSet, 'region')
router.register('category', CategoryModelViewSet, 'category')
# router.register('blog', BlogModelViewSet, 'blog')
router.register('blog', BlogDocumentViewSet, 'blog')

urlpatterns = [
    path('', include(router.urls)),
]
