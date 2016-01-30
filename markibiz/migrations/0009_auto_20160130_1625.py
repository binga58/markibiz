# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markibiz', '0008_event_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='about',
            field=models.TextField(null=True, blank=True),
        ),
    ]
