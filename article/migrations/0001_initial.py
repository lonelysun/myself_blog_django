# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-26 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
