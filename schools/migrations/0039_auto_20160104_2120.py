# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 05:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0038_auto_20160104_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classhomework',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]