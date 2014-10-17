# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import article.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20141011_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=datetime.date(2014, 10, 11), upload_to=article.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
