# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-28 14:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modulos', '0003_auto_20170920_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.NullBooleanField()),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_termino', models.DateField(blank=True, null=True)),
                ('porcent', models.IntegerField(default=0)),
                ('estado', models.CharField(max_length=20)),
                ('user_asign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsable2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='carpeta',
            name='default',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='modulo',
            name='default',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='submodulo',
            name='default',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='submodulo',
            name='proceso',
            field=models.ManyToManyField(blank=True, null=True, related_name='proceso', to='modulos.Proceso'),
        ),
    ]