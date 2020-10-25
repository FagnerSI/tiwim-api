from django.db import models


class Role(models.Model):

    class Meta:

        db_table = 'role'

    name = models.CharField('Nome', max_length=100, blank=True)

    def __str__(self):
        return self.name
