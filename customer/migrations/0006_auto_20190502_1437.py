# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-02 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_barangmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangmodel',
            name='harga',
            field=models.CharField(max_length=10),
        ),
    ]
