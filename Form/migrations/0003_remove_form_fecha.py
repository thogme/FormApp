# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 03:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0002_form_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='fecha',
        ),
    ]