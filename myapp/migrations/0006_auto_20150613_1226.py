# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_instructor_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(null=True, to='myapp.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='myapp.Student'),
        ),
    ]
