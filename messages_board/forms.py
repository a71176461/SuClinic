# -*- coding: utf-8 -*-
__author__ = 'huangpinjie'


from django import forms
from captcha.fields import CaptchaField



class PostForm(forms.Form):

    name = forms.CharField(max_length=50, required=True)
    content = forms.CharField(max_length=500, widget=forms.Textarea())
    captcha = CaptchaField()

    def clean_content(self):
        content = self.cleaned_data['content']

        if len(content) < 5:
            raise forms.ValidationError('字數不足')

        # # 验证码
        # try:
        #     captcha = self.cleaned_data['captcha']
        # except Exception as e:
        #     print 'except: '+ str(e)
        #     raise forms.ValidationError('wrong')

        return content