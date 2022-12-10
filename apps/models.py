import uuid

from django.db.models import Model, ForeignKey, CharField, ImageField, UUIDField, TextField, CASCADE, ManyToManyField


class Region(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'


class Category(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Tag(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=125)

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtaglar'


class Blog(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=55)
    text = TextField()
    image = ImageField(upload_to='blogs/%Y/%m/%d')
    category = ForeignKey('apps.Category', CASCADE)
    region = ForeignKey('apps.Region', CASCADE, null=True, blank=True)
    tag = ManyToManyField('apps.Tag')
