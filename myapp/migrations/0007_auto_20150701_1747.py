# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20150613_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('country', models.CharField(default='Canada', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='myapp.Authors'),
        ),
    ]
