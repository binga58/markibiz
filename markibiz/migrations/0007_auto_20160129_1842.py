# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markibiz', '0006_auto_20160129_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='organizer_number',
        ),
        migrations.AlterField(
            model_name='event',
            name='oraganizer',
            field=models.ForeignKey(to='markibiz.Team'),
        ),
    ]
