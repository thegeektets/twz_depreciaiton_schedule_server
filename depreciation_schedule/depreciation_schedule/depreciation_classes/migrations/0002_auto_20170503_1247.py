# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depreciation_classes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssetClass',
            new_name='DepreciationClass',
        ),
    ]
