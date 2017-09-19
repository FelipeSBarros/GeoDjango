# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Municipios

#def points_view(request):
#    points_as_geojson = serialize('geojson', Point.objects.all())
#    return HttpResponse(points_as_geojson, content_type='json')

def mun_view(request):
    municipios_as_geojson = serialize('geojson', Municipios.objects.all())
    return HttpResponse(municipios_as_geojson, content_type='json')
    
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'index.html'
