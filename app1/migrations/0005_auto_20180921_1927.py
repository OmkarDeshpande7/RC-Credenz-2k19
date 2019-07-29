# Generated by Django 2.1.1 on 2018-09-21 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_merge_20180921_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_1',
            field=models.EmailField(default='player_1@gmail.com', max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email_2',
            field=models.EmailField(default='player_2@gmail.com', max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name_1',
            field=models.CharField(default='player_1', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name_2',
            field=models.CharField(default='player_2', max_length=100),
        ),
    ]
