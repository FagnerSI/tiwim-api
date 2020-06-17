# Generated by Django 2.2 on 2020-06-14 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('members', models.ManyToManyField(related_name='topics', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='project.Project', verbose_name='Projeto')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
    ]
