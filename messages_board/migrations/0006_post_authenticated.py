# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_board', '0005_auto_20160301_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='authenticated',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
