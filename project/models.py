from django.db import models

from account.models import Account
from role.models import Role


class Project(models.Model):

    class Meta:
        db_table = 'project'

    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    """ created_by = models.ForeignKey(
        Account, related_name="projects_create_by_me", on_delete=models.CASCADE) """
    members = models.ManyToManyField(Account, related_name='projects')
    roles = models.ManyToManyField(Role, related_name="projects")

    def __str__(self):
        return self.name


""" class Users_Projects(models.Model):
    user = models.ForeignKey(
        Account, related_name='projects', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    admin = models.BooleanField('É administrador?', default=False) """
