# Generated by Django 2.2 on 2020-06-14 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='project.Project')),
            ],
            options={
                'db_table': 'role',
            },
        ),
    ]
