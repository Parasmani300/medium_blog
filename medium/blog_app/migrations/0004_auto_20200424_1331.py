# Generated by Django 2.2.5 on 2020-04-24 08:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20200424_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 4, 24, 8, 1, 9, 733383, tzinfo=utc)),
        ),
    ]