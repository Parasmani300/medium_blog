# Generated by Django 2.2.5 on 2020-04-24 08:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_auto_20200424_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 4, 24, 8, 8, 44, 282462, tzinfo=utc)),
        ),
    ]
