# Generated by Django 2.2 on 2020-10-23 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatemodel',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 16, 3, 6, 153982)),
        ),
    ]