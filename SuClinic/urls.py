"""SuClinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from SuClinic import settings
from SuClinic.views import IndexView, ClinicScheduleView
from django.views.generic import TemplateView
from django.contrib.staticfiles import views
from article.views import BlogIndexListView, Categories, BlogCategoryListView, BlogDetailView
from messages_board.views import PostView


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^captcha/', include('captcha.urls')),


    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^clinic_schedule/$', ClinicScheduleView.as_view(), name='clinic_schedule'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^static/(?P<path>.*)$', views.serve),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^blog_list/$', BlogIndexListView.as_view(), name='blog_index'),

    url(r'^blog/blog_detail/(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>\d+)/$', BlogCategoryListView.as_view()),
    url(r'^messages_board/$', PostView.as_view(), name='messages_board'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
