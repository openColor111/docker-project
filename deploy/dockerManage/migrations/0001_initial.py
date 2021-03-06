# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=256)),
                ('docker_id', models.CharField(max_length=128)),
                ('ip', models.GenericIPAddressField(protocol='ipv4')),
                ('port', models.IntegerField()),
            ],
        ),
    ]
