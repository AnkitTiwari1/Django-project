# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-21 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Information',
        ),
    ]
