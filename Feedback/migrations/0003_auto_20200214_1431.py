# Generated by Django 3.0.2 on 2020-02-14 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0002_auto_20200214_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Expiry',
            field=models.DurationField(default=datetime.timedelta(days=20, seconds=36000)),
        ),
    ]
