# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger_hunt', '0003_auto_20161209_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('hunt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scavenger_hunt.ScavengerHunt')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
