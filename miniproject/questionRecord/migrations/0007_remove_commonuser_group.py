# Generated by Django 3.1.7 on 2021-08-09 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionRecord', '0006_auto_20210809_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonuser',
            name='group',
        ),
    ]