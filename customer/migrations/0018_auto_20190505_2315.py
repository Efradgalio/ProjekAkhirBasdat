# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20190505_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangmodel',
            name='gambar',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]