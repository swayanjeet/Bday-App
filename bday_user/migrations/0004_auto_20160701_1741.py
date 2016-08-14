# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 12:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bday_user', '0003_auto_20160701_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bday_app_user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_bday_app_user_friends_+', to='bday_user.Bday_App_User'),
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='google_plus_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='pic',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]