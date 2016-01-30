# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markibiz', '0005_auto_20160129_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='level',
            field=models.CharField(choices=[('JUNIOR', 'JUNIOR'), ('SENIOR', 'SENIOR')], max_length=6),
        ),
    ]
