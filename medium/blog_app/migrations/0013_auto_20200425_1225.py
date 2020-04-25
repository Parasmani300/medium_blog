# Generated by Django 2.2.5 on 2020-04-25 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_auto_20200425_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='replacer',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 4, 25, 6, 55, 50, 464068, tzinfo=utc)),
        ),
    ]
