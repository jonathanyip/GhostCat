# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('post_text', models.CharField(max_length=140)),
                ('post_date', models.DateTimeField()),
                ('post_author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
