# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 13:33
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_auto_20170918_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cd_geocodm', models.CharField(max_length=20)),
                ('nm_municip', models.CharField(max_length=60)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='lim_unidade_federacao_a',
        ),
    ]