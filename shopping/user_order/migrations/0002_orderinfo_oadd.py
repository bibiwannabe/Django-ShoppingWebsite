# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='oadd',
            field=models.CharField(default='', max_length=100),
        ),
    ]
