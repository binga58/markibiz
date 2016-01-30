# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('oraganizer', models.CharField(max_length=128)),
                ('organizer_number', models.IntegerField(verbose_name='Organizer Number', max_length=12)),
                ('prize', models.IntegerField()),
                ('poster', models.ImageField(null=True, upload_to='event_img/')),
                ('registration_start', models.DateTimeField()),
                ('registration_end', models.DateTimeField()),
                ('event_start', models.DateTimeField()),
                ('event_end', models.DateTimeField()),
                ('active', models.BooleanField()),
                ('sponsor', models.CharField(null=True, max_length=128, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
