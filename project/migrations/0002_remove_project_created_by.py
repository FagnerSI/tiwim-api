# Generated by Django 2.2 on 2020-06-14 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
    ]
