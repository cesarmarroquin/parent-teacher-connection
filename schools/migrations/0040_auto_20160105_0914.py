# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0039_auto_20160104_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classform',
            name='file',
            field=models.FileField(null=True, upload_to='class_forms/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='classform',
            name='message',
            field=models.TextField(default='message goes here'),
        ),
        migrations.AlterField(
            model_name='classform',
            name='subject',
            field=models.TextField(default='subject goes here'),
        ),
        migrations.AlterField(
            model_name='classform',
            name='title',
            field=models.CharField(default='title goes here', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentform',
            name='signer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentform',
            name='title',
            field=models.CharField(default='title goes here', max_length=255),
        ),
    ]
