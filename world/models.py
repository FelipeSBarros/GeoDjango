# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
#from django.contrib.gis.db import models
#class lim_unidade_federacao_a(models.Model):
#	nome = models.CharField(max_length = 100)
#	nomeabrev = models.CharField(max_length = 50)
#	geometriaaproximada = models.CharField(max_length = 3)
# 	sigla = models.CharField(max_length = 3)
#	geocodigo = models.CharField(max_length = 15)
#	geom = models.MultiPolygonField(srid=4674)
#	tx_comentario_producao = models.CharField(max_length = 250)
#	id_produtor = models.IntegerField('id_produtor')
#	id_elementoprodutor = models.IntegerField('id_elementoprodutor')
#	
#	def __str__(self):
#		return self.nome
# Create your models here.

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Municipios(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cd_geocodm = models.CharField(max_length=20)
    nm_municip = models.CharField(max_length=60)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
      return self.nm_municip
# Auto-generated `LayerMapping` dictionary for Municipios model
municipios_mapping = {
    'id' : 'ID',
    'cd_geocodm' : 'CD_GEOCODM',
    'nm_municip' : 'NM_MUNICIP',
    'geom' : 'MULTIPOLYGON',
}
