# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-09 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_form',
            name='email',
        ),
        migrations.RemoveField(
            model_name='room_form',
            name='name',
        ),
        migrations.AlterField(
            model_name='room_form',
            name='room_no',
            field=models.CharField(max_length=4),
        ),
    ]
