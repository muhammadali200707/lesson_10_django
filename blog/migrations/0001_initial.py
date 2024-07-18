# Generated by Django 5.0.7 on 2024-07-14 03:43

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('publish', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog/blog/')),
                ('status', models.CharField(choices=[('pb', 'Publish'), ('df', 'DRAFT')], default='pb', max_length=4)),
                ('publish', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 8, 43, 10, 238444))),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ManyToManyField(to='blog.comments')),
            ],
        ),
    ]
