# Generated by Django 3.0.2 on 2020-02-14 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0006_auto_20200214_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='Feedbacks',
        ),
    ]
