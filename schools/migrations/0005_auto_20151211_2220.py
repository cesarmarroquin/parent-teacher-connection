# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_remove_classfee_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassFeePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('charge_id', models.CharField(max_length=255, null=True)),
                ('refunded', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='classfee',
            name='charge_id',
        ),
        migrations.RemoveField(
            model_name='classfee',
            name='refunded',
        ),
        migrations.AddField(
            model_name='classfeepayment',
            name='class_fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.ClassFee'),
        ),
        migrations.AddField(
            model_name='classfeepayment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.Student'),
        ),
    ]