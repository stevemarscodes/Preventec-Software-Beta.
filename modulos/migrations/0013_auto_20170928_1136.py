# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-28 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0012_remove_carpeta_is_subcarpeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpeta',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]