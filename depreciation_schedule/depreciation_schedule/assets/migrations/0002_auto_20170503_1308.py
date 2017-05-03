# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depreciation_classes', '0003_auto_20170503_1308'),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='asset_class',
        ),
        migrations.AddField(
            model_name='asset',
            name='depreciation_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='depreciation_classes.DepreciationClass'),
        ),
    ]