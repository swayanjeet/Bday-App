# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bday_user', '0004_auto_20160701_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bday_app_user',
            old_name='activated',
            new_name='available',
        ),
        migrations.AlterField(
            model_name='bday_app_user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_bday_app_user_friends_+', to='bday_user.Bday_App_User'),
        ),
    ]
