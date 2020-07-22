from django.db import models

from account.models import Account
from role.models import Role
from topic.models import Topic


class Replay(models.Model):

    KIND_OF_SPEECH_CHOICES = (
        ('PE', 'Pergunto'),
        ('SU', 'Sugiro'),
        ('AD', 'Além disso'),
        ('CM', 'Comento'),
        ('ACT', 'Acrescento'),
        ('INF', 'Informo'),
        ('RP', 'Respondo'),
        ('CD', 'Concordo'),
        ('DIS', 'Discordo'),
        ('PRQ', 'Para que'),
        ('PQ', 'Porque'),
        ('PC', 'Peço'),
        ('EX', 'Explico'),
        ('EXF', 'Exemplifico'),
        ('NE', 'Não entendi'),
        ('E', 'E'),
        ('ET', 'Então'),
        ('OU', 'Ou'),
        ('MAS', 'Mas'),
        ('CNM', 'Concordo mas'),
        ('DSM', 'Discordo mas'),
        ('CON', 'Continuo'),
        ('TRN', 'Transcrevo'),
    )

    class Meta:
        db_table = 'replay'

    description = models.TextField('Descrição', blank=True)

    kind_speech = models.CharField(
        'Tipo de fala',
        max_length=10,
        choices=KIND_OF_SPEECH_CHOICES,
        default='E',
    )

    roles_in = models.ForeignKey(
        Role, verbose_name='No papel', related_name='replays_in',  on_delete=models.CASCADE)

    roles_for = models.ManyToManyField(
        Role, verbose_name='Para o papel', related_name='replays_for')

    url_details = models.TextField('uri', blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    author = models.ForeignKey(Account, verbose_name='User',
                               related_name='replays', on_delete=models.CASCADE)
    topic = models.ForeignKey(
        Topic, verbose_name='Topic', related_name='replays', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
