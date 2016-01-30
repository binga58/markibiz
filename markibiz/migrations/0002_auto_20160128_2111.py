# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markibiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer_number',
            field=models.IntegerField(verbose_name='Organizer Number'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_start',
            field=models.DateField(),
        ),
    ]
