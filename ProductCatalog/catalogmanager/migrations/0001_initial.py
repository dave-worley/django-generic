# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('width', models.FloatField()),
                ('length', models.FloatField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('value', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
    ]
