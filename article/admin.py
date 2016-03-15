# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget

# Register your models here.

from article.models import Blog
from article.models import Categories
from image_cropping import ImageCroppingMixin, ImageCropWidget

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

class BlogAdminForm(ImageCroppingMixin, forms.ModelForm):

    class Meta:
        model = Blog
        # widgets = {
        #     'image': ImageCropWidget,
        # }
        # 不顯示建立時間和更改時間
        exclude = (
            'create_time',
            'modify_time',
            'slug',
        )


class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title', )}
    list_display = [
        'title',
        'category',
        'create_time',
        'modify_time',
        'images',
    ]

    form = BlogAdminForm


admin.site.register(Blog, BlogAdmin)
admin.site.register(Categories, CategoriesAdmin)
