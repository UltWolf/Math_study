# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theory', '0004_auto_20170320_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maththeory',
            name='image',
            field=models.ImageField(blank=True, upload_to='theory_images'),
        ),
    ]