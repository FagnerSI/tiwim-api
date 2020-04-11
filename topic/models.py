from django.db import models

from user.models import User
from project.models import Project


class Topic(models.Model):

    class Meta:
        db_table = 'topic'

    title = models.CharField(max_length=200)
    description = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    users = models.ManyToManyField(User)

    project = models.ForeignKey(
        Project, verbose_name='Projeto', related_name='topics',  on_delete=models.CASCADE)

    def __str__(self):
        return self.title
