# Generated by Django 3.1.7 on 2021-08-09 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionRecord', '0004_auto_20210809_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonuser',
            name='lastCheckDate',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 0, 0)),
        ),
    ]
