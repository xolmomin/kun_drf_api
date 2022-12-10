from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import RegionModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register('region', RegionModelViewSet, 'region')
router.register('category', CategoryModelViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
]

'''

modellar

blog
category
region
tag

filter
tag boyicha
region boyicha
category boyicha


'''
