# Generated by Django 2.2.5 on 2020-04-25 07:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_auto_20200425_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 4, 25, 7, 15, 26, 369731, tzinfo=utc)),
        ),
    ]
