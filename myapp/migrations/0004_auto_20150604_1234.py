# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150602_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('subject', models.CharField(max_length=100, unique=True)),
                ('intro_course', models.BooleanField(default=True)),
                ('time', models.IntegerField(choices=[(0, 'No preference'), (1, 'Morning'), (2, 'Afternoon'), (3, 'Evening')], default=0)),
                ('num_responses', models.IntegerField(default=0)),
                ('avg_age', models.IntegerField(default=20)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
