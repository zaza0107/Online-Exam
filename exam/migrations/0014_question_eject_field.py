# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_remove_candidate_choice_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='eject_field',
            field=models.BooleanField(default=False),
        ),
    ]
