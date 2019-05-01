# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-01 05:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0003_remove_tokomodel_nama_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokomodel',
            name='nama_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]