# -*- coding: utf-8 -*-
__author__ = 'huangpinjie'


from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect, get_object_or_404, Http404
from article.models import Blog, Categories
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.contrib.contenttypes.models import ContentType
from django.views.generic.detail import DetailView, SingleObjectMixin

# Create your views here.



# 分類的基礎類別
class CategoryViewMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CategoryViewMixin, self).get_context_data(**kwargs)
        context.update({
            'categories': Categories.objects.all().order_by('name'),
        })
        return context


class BlogIndexView(object):
    model = Blog

    def dispatch(self, request, *args, **kwargs):
        # 用dispatch方式實現get傳遞slug
        return super(BlogIndexView, self).dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     return super(BlogIndexView, self).get_queryset().order_by('-time')

class BlogIndexListView(BlogIndexView, CategoryViewMixin, ListView):
    paginate_by = 4
    template_name = 'article_index.html'


class BlogDetailView(BlogIndexView, CategoryViewMixin, DetailView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog_detail'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context.update({
            'categories': Categories.objects.all().order_by('name'),
        })
        if not self.object.images:
            crop = False

        else:
            crop = True

        context.update({
            'crop': crop,
        })
        # try:
        #     crop = self.get_context_data(**kwargs)
        # except self.object.images:
        #     crop = False

        return context

# 分類文章列表
class BlogCategoryView(SingleObjectMixin, CategoryViewMixin, ListView):

    def get(self, request, *args, **kwargs):
        # 傳遞物件為Categories
        self.object = self.get_object(queryset=Categories.objects.all())
        return super(BlogCategoryView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        # 取得此Categories的所有文章
        return self.object.blog_set.all()

class BlogCategoryListView(BlogCategoryView):
    paginate_by = 4
    template_name = "article_list_category.html"
