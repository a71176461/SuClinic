from __future__ import absolute_import
__author__ = 'huangpinjie'


from django import forms

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField


class CkEditorForm(forms.Form):
    content = RichTextFormField()
    content_upload = RichTextUploadingField()


