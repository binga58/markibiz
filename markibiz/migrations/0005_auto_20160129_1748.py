# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markibiz', '0004_auto_20160129_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_start',
            field=models.DateTimeField(),
        ),
    ]
