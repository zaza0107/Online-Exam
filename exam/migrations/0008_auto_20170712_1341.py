# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20170712_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate_choice',
            old_name='candidate_choice',
            new_name='candidate_question',
        ),
    ]