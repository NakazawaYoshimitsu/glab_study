# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-23 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0005_auto_20160922_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='bihin',
            name='bihin_type',
            field=models.IntegerField(choices=[(0, 'ノートパソコン'), (1, 'デスクトップパソコン')], default=0, verbose_name='種別'),
            preserve_default=False,
        ),
    ]
