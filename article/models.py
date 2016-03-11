# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from image_cropping import ImageRatioField
from django.core import validators
import uuid
import re
from django.utils.translation import gettext as _

# Create your models here.


"""
Categories：文章分類
Blog：文章
"""
class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    # 發布時間
    time = models.DateTimeField()
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='blog/images', blank=True)

    # 裁切後的照片，用於文章上方
    cropping = ImageRatioField('images.url', '1920x650')
    author = models.CharField(max_length=100)

    # slug用於在url上傳遞文章的路徑標記，並使用uuid產生之代碼當作文章的獨立識別碼。
    # 如：blog/blog_detail/(?P<slug>[-\w]+)/$。
    slug = models.SlugField(
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[a-zA-Z-0-9_]+$'),
                _(u"請輸入正確的識別碼"),
                'invalid')
        ],
        help_text=_(u"僅支援 a-z、A-Z、-、0-9 或 _ 中的任一字元。"),
    )
    category = models.ForeignKey(Categories)

    # 取的url並且回傳slug
    @models.permalink
    def get_absolute_url(self):
        return ('blog', [self.slug])

    # 使用ckeditor的RichTextUploading來做編輯文章內容
    content_upload = RichTextUploadingField('文章內容', default='', null=True, blank=True)

    create_time = CreationDateTimeField(db_index=True,)

    modify_time = ModificationDateTimeField(db_index=True,)

    def __unicode__(self):
        return self.title

    class Meta:
        # 用最新時間做排序
        ordering = ['-time']


