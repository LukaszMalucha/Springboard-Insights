# Generated by Django 2.1.5 on 2020-01-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='ects_credits',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='nfq',
            field=models.CharField(default='0', max_length=255),
        ),
    ]