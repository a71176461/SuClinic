# -*- coding: utf-8 -*-
from __future__ import absolute_import
__author__ = 'huangpinjie'


from django.shortcuts import render_to_response, RequestContext
from django.views.generic.base import View, TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ClinicScheduleView(TemplateView):
    template_name = 'clinic_schedule.html'


