import random

from django.core.management import BaseCommand
from faker import Faker

from apps.models import Blog, Category, Region

fake = Faker()


class Command(BaseCommand):
    help = '''
        You can create dummy data. Like this:
    * Blogs      -> 1000
    * Categories    -> 15
    '''

    def add_arguments(self, parser):
        parser.add_argument('-b', '--blog', type=int, help='Define a blog number prefix', )
        parser.add_argument('-c', '--category', type=int, help='Define a category number prefix', )

    def handle(self, *args, **options):

        b = options['blog'] if options['blog'] else 0
        c = options['category'] if options['category'] else 0

        if c:
            # Create 10 dummy data Category
            for i in range(c):
                Category.objects.create(name=fake.text(50))
            print('category added', c)

        if b:
            categories = Category.objects.all()
            regions = Region.objects.all()
            for i in range(b):
                Blog.objects.create(
                    title=fake.text(55),
                    text=fake.sentence(1000),
                    region=random.choice(regions),
                    category=random.choice(categories),
                    image='https://via.placeholder.com/720x480'
                )
            print('blog added', b)
