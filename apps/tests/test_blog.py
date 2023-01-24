import random
from uuid import UUID
from faker import Faker
from model_bakery import baker
import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from apps.models import Blog, Tag, Region, Category


@pytest.mark.django_db
class TestBlogView:

    @pytest.fixture
    def blog(self):
        return baker.make(Blog)

    @pytest.fixture
    def blogs(self):
        faker = Faker()
        region = baker.make('apps.Region', _quantity=12)
        category = baker.make('apps.Category', _quantity=5)
        tags_set = baker.make('apps.Tag', _quantity=10)

        baker.make(
            Blog,
            _quantity=10,
            title=faker.text()[:50],
            text=faker.text(),
            image=faker.file_name(category='image', extension='jpeg'),
            region=random.choice(region),
            category=random.choice(category),
            tag=tags_set,
        )

    def test_create_blog_model(self, blogs):
        category = Category.objects.first()
        faker = Faker()
        blog = Blog.objects.create(
            title='New Blog',
            text='text description',
            # image=
            image=faker.file_name(category='image', extension='jpeg'),
            category=category,
        )
        count = Blog.objects.count()
        assert count == 11
        assert blog.title == 'New Blog'
        assert blog.text == 'text description'
        assert blog.category == category

    def test_update_blog_model(self, blog):
        title = 'NEW TITLE'
        blog.title = title
        blog.save()
        assert blog.title == title

    def test_blog_list_api(self, client, blogs):
        url = reverse_lazy('blog-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10


    #
    # def test_create_blog_api(self, client):
    #     url = reverse_lazy('blog-list')
    #     data = {
    #         'name': 'Toshkent'
    #     }
    #     response = client.post(url, data)
    #     assert response.status_code == 201
    #     assert response.data['name'] == data['name']
    #     assert len(response.data['id']) == 36
    #
    # @pytest.fixture()
    # def blogs(self):
    #     Blog.objects.create(name='Toshkent')
    #     Blog.objects.create(name='Navoi')
    #
    # def test_blog_list_api(self, client, blogs):
    #     url = reverse_lazy('blog-list')
    #     # url = '/api/v1/blog/'
    #     response = client.get(url)
    #     assert response.status_code == 200
    #     assert len(response.data) == 2
    #
    # def test_blog_update_api(self, client, blogs):
    #     blog = Blog.objects.first()
    #     '/api/v1/blog/e09c9c1e-c071-4e4e-bc6f-76fc2b67d5f5/'
    #     url = reverse_lazy('blog-detail', args=(blog.pk,))
    #     data = {
    #         'name': 'Fargona'
    #     }
    #     response = client.patch(url, data, content_type='application/json')
    #     assert response.status_code == 200
    #     assert response.data['name'] == data['name']
    #     assert response.data['id'] == str(blog.pk)
    #
    # def test_blog_filter_api(self, client, blogs):
    #     blog = Blog.objects.first()
    #     '/api/v1/blog?name=Fargona'
    #     url = reverse_lazy('blog-list')
    #     data = {
    #         'name': 'Toshkent'
    #     }
    #     response = client.get(url, data, content_type='application/json')
    #     assert response.status_code == 200
    #     assert response.data[0]['name'] == data['name']
    #     assert response.data[0]['id'] == str(blog.pk)
    #     assert len(response.data) == 1
    #
    # def test_blog_wrong_filter_api(self, client, blogs):
    #     blog = Blog.objects.first()
    #     '/api/v1/blog?name=Samarqand'
    #     url = reverse_lazy('blog-list')
    #     data = {
    #         'name': 'Samarqand'
    #     }
    #     response = client.get(url, data, content_type='application/json')
    #     assert response.status_code == 200
    #     assert len(response.data) == 0

#
# websocket, elasticsearch
#
