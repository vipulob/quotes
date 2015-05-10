# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_text', models.CharField(max_length=500)),
                ('average_rating', models.IntegerField(default=0)),
                ('user_who_uploaded_id', models.IntegerField(default=0)),
            ],
        ),
    ]
