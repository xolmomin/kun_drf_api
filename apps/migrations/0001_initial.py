# Generated by Django 4.1.4 on 2023-01-17 16:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': "Bo'lim",
                'verbose_name_plural': "Bo'limlar",
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Hashtag',
                'verbose_name_plural': 'Hashtaglar',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=55)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='blogs/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.category')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.region')),
                ('tag', models.ManyToManyField(to='apps.tag')),
            ],
        ),
    ]
