# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-23 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0008_bihin_bihin_manufct'),
    ]

    operations = [
        migrations.AddField(
            model_name='bihin',
            name='bihin_rdate',
            field=models.DateField(default=1977, verbose_name='リース期限'),
            preserve_default=False,
        ),
    ]