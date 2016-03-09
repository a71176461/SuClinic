# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 11:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160227_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, help_text='\u50c5\u652f\u63f4 a-z\u3001A-Z\u3001- \u6216 _ \u4e2d\u7684\u4efb\u4e00\u5b57\u5143\u3002', unique=True, validators=[django.core.validators.RegexValidator(re.compile(b'^[a-zA-Z-_]+$'), '\u8acb\u8f38\u5165\u6b63\u78ba\u7684\u8b58\u5225\u78bc', b'invalid')]),
        ),
    ]
