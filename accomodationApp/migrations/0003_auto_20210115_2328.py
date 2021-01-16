# Generated by Django 3.1.5 on 2021-01-15 22:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodationApp', '0002_auto_20210115_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='mobileNumber',
            field=models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(13)]),
        ),
    ]
