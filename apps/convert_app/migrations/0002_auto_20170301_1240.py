# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='uploaded_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.URLField(blank=True, verbose_name='Reposit\xf3rio'),
        ),
    ]
