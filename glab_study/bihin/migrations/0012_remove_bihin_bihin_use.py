# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-23 04:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0011_bihin_bihin_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bihin',
            name='bihin_use',
        ),
    ]
