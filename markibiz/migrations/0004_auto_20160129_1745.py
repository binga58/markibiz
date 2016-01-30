# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('markibiz', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('about', models.TextField()),
                ('post', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='team_img/', null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('level', models.CharField(max_length=6, choices=[('JUNIOR', 'JUNIOR'), ('SENIOR', 'SENIOR'), ('L', 'Large')])),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='registration_link',
            field=models.URLField(default=datetime.datetime(2016, 1, 29, 12, 15, 25, 681274, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
