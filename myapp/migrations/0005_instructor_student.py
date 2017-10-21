# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('myapp', '0004_auto_20150604_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('webpage', models.URLField()),
                ('office', models.CharField(max_length=100, default='EH 120')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.IntegerField()),
                ('level', models.IntegerField(default=1, choices=[(1, 'Undergrad'), (2, 'Masters'), (3, 'PhD')])),
            ],
        ),
    ]
