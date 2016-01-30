# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markibiz', '0007_auto_20160129_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='speaker',
            field=models.BooleanField(default=False),
        ),
    ]
