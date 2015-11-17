# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='imagen',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
