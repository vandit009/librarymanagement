# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=50)),
                ('birthdate', models.IntegerField()),
                ('country', models.CharField(max_length=50, default='Canada')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('numpages', models.IntegerField(null=True)),
                ('in_stock', models.BooleanField(verbose_name=True)),
                ('pubyear', models.DateField(null=True)),
                ('author', models.ManyToManyField(to='myapp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.AutoField(serialize=False, primary_key=True)),
                ('textbook', models.ForeignKey(to='myapp.Book')),
            ],
        ),
    ]
