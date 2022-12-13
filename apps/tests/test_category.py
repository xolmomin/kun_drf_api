from uuid import UUID

import pytest
from django.urls import reverse_lazy

from apps.models import Category


@pytest.mark.django_db  # check model
def test_create_model_category():
    category = Category.objects.create(name='Boshqalar')
    count = Category.objects.count()
    assert isinstance(category.pk, UUID)
    assert category.name == 'Boshqalar'
    assert count == 1


@pytest.mark.django_db  # check api
def test_create_category_api(client):
    url = reverse_lazy('category-list')
    data = {
        'name': 'Boshqalar'
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == data['name']
    assert len(response.data['id']) == 36


@pytest.fixture
def categories():
    Category.objects.create(name='Uy-joy')
    Category.objects.create(name='Texnika')


@pytest.mark.django_db
def test_category_list_api(client, categories):
    url = reverse_lazy('category-list')
    # url = '/api/v1/category/'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_category_update_api(client, categories):
    category = Category.objects.first()
    '/api/v1/category/e09c9c1e-c071-4e4e-bc6f-76fc2b67d5f5/'
    url = reverse_lazy('category-detail', args=(category.pk, ))
    data = {
        'name': 'Kiyim-kechak'
    }
    response = client.patch(url, data, content_type='application/json')
    assert response.status_code == 200
    assert response.data['name'] == data['name']
    assert response.data['id'] == str(category.pk)

