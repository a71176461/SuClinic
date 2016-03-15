# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from django.utils.translation import gettext as _

# Create your models here.

class Post(models.Model):
    # 文章建立時間
    date_time = CreationDateTimeField(verbose_name=_(u'建立時間'),)

    # 判斷此文章是否為有帳號所有人的文章。
    authenticated = models.BooleanField(
        db_index=True,
        default=False,
    )

    # 留言者名稱
    name = models.CharField(max_length=50, verbose_name=_(u'訪客名稱'),)

    # 留言內容
    content = models.CharField(max_length=500, verbose_name=_(u'訪客內文'),)

    # 官方回應內容
    response = models.CharField(max_length=500, blank=True, verbose_name=_(u'回覆'),)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-date_time']
        # permissions = (
        #     ("can_comment", "Can comment"),
        # )

