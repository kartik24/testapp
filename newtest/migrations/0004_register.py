# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest', '0003_auto_20170622_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=200)),
                ('Password', models.CharField(max_length=20)),
                ('Number', models.IntegerField(max_length=10)),
                ('City', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Register',
            },
        ),
    ]
