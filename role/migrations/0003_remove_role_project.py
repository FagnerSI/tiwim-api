# Generated by Django 2.2 on 2020-10-17 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0002_auto_20201017_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='project',
        ),
    ]
