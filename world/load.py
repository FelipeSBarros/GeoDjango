import os
from django.contrib.gis.utils import LayerMapping
from .models import Municipios

Mun_mapping = {
	'id' : 'ID',
    'cd_geocodm' : 'CD_GEOCODM',
    'nm_municip' : 'NM_MUNICIP',
    'geom' : 'MULTIPOLYGON',
    }

mun_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Mun.shp'),)
def run(verbose=True):
	lm = LayerMapping(Municipios, mun_shp, Mun_mapping, transform=False, encoding = 'LATIN1',)
	lm.save(strict=True, verbose=verbose)
