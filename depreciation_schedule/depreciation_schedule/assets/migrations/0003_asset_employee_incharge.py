# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 13:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0002_auto_20170503_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='employee_incharge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]