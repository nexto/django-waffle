# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.WAFFLE_CUSTOM_ACCOUNT_MODEL),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='accounts',
            field=models.ManyToManyField(help_text='Activate this flag for these accounts.', to=settings.WAFFLE_CUSTOM_ACCOUNT_MODEL, blank=True),
        ),
    ]
