# Generated by Django 5.0.7 on 2024-07-18 14:03

import course.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_options_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=course.helpers.SaveMediaFiles.save_course_image),
        ),
    ]
