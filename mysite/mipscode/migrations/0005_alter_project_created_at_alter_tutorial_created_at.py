# Generated by Django 4.1.3 on 2022-12-27 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipscode', '0004_documentation_alter_project_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 17, 2, 38, 312820, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 17, 2, 38, 312820, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
    ]