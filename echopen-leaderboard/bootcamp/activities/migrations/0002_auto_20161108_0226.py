# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-08 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_auto_20161030_2333'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='run',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='run',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Algorithm'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[(b'L', b'Liked'), (b'C', b'Commented'), (b'F', b'Favorited'), (b'A', b'Answered'), (b'W', b'Accepted Answer'), (b'E', b'Edited Article'), (b'S', b'Also Commented'), (b'R', b'Run is done')], max_length=1),
        ),
    ]