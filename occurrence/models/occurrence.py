from django.db import models


class Occurrence(models.Model):
    description = models.TextField(null=False, blank=False, verbose_name='Descrição')
    category = models.CharField(max_length=255, verbose_name='Categoria')
    preciseDate = models.DateField()
    startDate = models.DateField()
    finishDate = models.DateField()

    def __str__(self):
        return self.description

    class Meta:
        abstract = False