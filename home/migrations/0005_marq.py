# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-24 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_marq'),
    ]

    operations = [
        migrations.CreateModel(
            name='marq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
