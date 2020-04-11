from django.db import models


class User(models.Model):

    class Meta:

        db_table = 'user'

    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    password = models.CharField('Senha', max_length=100, null=True)

    is_active = models.BooleanField('Está ativo?', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    def __str__(self):
        return self.name
