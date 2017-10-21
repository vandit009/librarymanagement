# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150530_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 6, 2, 15, 13, 35, 654889, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_no',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
