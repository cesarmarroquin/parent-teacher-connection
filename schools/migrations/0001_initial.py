# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parents', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ManyToManyField(to='parents.Parent')),
                ('school_class', models.ManyToManyField(to='schools.SchoolClass')),
            ],
        ),
    ]
