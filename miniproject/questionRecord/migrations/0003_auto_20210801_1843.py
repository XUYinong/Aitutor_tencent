# Generated by Django 3.1.7 on 2021-08-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionRecord', '0002_auto_20210801_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='conceptName',
            field=models.CharField(max_length=100),
        ),
    ]