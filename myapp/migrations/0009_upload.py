# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20150701_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
