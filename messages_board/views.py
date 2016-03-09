# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django import forms
from django.views.generic.edit import FormView, UpdateView
from messages_board.forms import PostForm
from messages_board.models import Post
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.utils import timezone
from django.views.generic.list import ListView
from django.http import HttpResponseForbidden
from django.views.generic.base import View, TemplateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json

# Create your views here.

# class PostListView(ListView):
#     def get_context_data(self, **kwargs):
#         context = super(PostListView, self).get_context_data(**kwargs)
#         # context.update({
#         #     'posts': Post.objects.all(),
#         # })
#         return context

class PostView(FormView, ListView):
    form_class = PostForm
    template_name = 'messages_board.html'
    success_url = '/messages_board/'
    model = Post
    context_object_name = 'comments'
    initial = {'content': u'', 'name': u'訪客'}
    paginate_by = 5

    def form_valid(self, form, **kwargs):
        if self.request.user.is_authenticated():
            Post.objects.create(
                # hide=form.cleaned_data['hide'],
                name=self.request.user,
                authenticated=True,
                content=form.cleaned_data['content'],
            )
        else:
            Post.objects.create(
                # hide=form.cleaned_data['hide'],
                name=form.cleaned_data['name'],
                content=form.cleaned_data['content'],
            )
        kwargs['object_list'] = Post.objects.all()
        self.object_list = Post.objects.all()
        return self.render_to_response(
            self.get_context_data(
                form=self.form_class(initial=self.initial), )
        )

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Post.objects.all()
        context = super(PostView, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.all(),
        })
        return context
    # def get_queryset(self):
    #     return super(PostView, self).get_queryset().order_by('-time')

