from django.db import models
from project.models import Project


class Role(models.Model):

    class Meta:

        db_table = 'role'

    name = models.CharField('Nome', max_length=100, blank=True)
    project = models.ForeignKey(
        Project, related_name="roles", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
