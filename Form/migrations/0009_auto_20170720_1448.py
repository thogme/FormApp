# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0008_auto_20170720_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('nombre', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='número')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
