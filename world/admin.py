# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.contrib import admin
from django.contrib.gis import admin
#from .models import lim_unidade_federacao_a
from .models import Municipios
admin.site.register(Municipios, admin.OSMGeoAdmin)

#admin.site.register(lim_unidade_federacao_a, admin.OSMGeoAdmin)
# Register your models here.
