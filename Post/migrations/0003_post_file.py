# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-23 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_remove_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
