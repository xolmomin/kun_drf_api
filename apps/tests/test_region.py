from uuid import UUID

import pytest
from django.urls import reverse_lazy, reverse

from apps.models import Region


@pytest.mark.django_db
class TestRegionView:
    def test_create_model_region(self):
        region = Region.objects.create(name='Toshkent')
        count = Region.objects.count()
        assert isinstance(region.pk, UUID)
        assert region.name == 'Toshkent'
        assert count == 1

    def test_create_region_api(self, client):
        url = reverse_lazy('region-list')
        data = {
            'name': 'Toshkent'
        }
        response = client.post(url, data)
        assert response.status_code == 201
        assert response.data['name'] == data['name']
        assert len(response.data['id']) == 36

    def test_region_list_api(self, client):
        Region.objects.create(name='Toshkent')
        Region.objects.create(name='Navoi')
        url = reverse_lazy('region-list')
        # url = '/api/v1/region/'
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_region_update_api(self, client):
        region = Region.objects.create(name='Toshkent')
        Region.objects.create(name='Navoi')
        url = reverse_lazy('region-detail', args=(region.pk,))
        data = {
            'name': 'Fargona'
        }
        response = client.patch(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['id'] == str(region.pk)

    @pytest.mark.django_db
    def test_region_filter_api(self, client):
        region = Region.objects.create(name='Toshkent')
        Region.objects.create(name='Navoi')
        url = reverse_lazy('region-list')
        data = {
            'name': 'Toshkent'
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data[0]['name'] == data['name']
        assert response.data[0]['id'] == f'{region.pk}'
        assert len(response.data) == 1

    def test_region_wrong_filter_api(self, client):
        Region.objects.create(name='Toshkent')
        Region.objects.create(name='Navoi')
        url = reverse_lazy('region-list')
        data = {
            'name': 'Samarqand'
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert len(response.data) == 0


# test, filter, factory-boy

