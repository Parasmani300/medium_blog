# Generated by Django 2.2.5 on 2020-04-24 08:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20200424_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 4, 24, 8, 3, 46, 17332, tzinfo=utc)),
        ),
    ]