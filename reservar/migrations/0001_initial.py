# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from decimal import Decimal
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('numero', models.CharField(max_length=200)),
                ('capacidad', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='photos')),
                ('precio', models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))),
                ('estado', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reservar',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descripcion', models.TextField()),
                ('fechacreado', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechainicio', models.DateTimeField(null=True, blank=True)),
                ('fechafinal', models.DateTimeField(null=True, blank=True)),
                ('Total', models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('habitacion', models.ForeignKey(to='reservar.Habitacion')),
            ],
        ),
    ]
