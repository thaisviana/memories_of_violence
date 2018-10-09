from django.db import models
from django.contrib.admin import ModelAdmin, site


class Occurrence(models.Model):
    description = models.TextField(null=False, blank=False, verbose_name='Descrição')
    category = models.CharField(max_length=255, verbose_name='Categoria')
    preciseDate = models.DateField(null=True, blank=True , verbose_name='Data precisa')
    startDate = models.DateField(null=True, blank=True , verbose_name='Data de início',
                                 help_text='Esta informação só deve ser inserida caso não haja uma data precisa')
    finishDate = models.DateField(null=True, blank=True , verbose_name='Data de fim',
                                  help_text='Esta informação só deve ser inserida caso não haja uma data precisa')
    location = models.ForeignKey('occurrence.Location', verbose_name="Localização", null=True, blank=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    @classmethod
    def register_admin(cls):
        site.register(cls, Admin)

    class Meta:
        abstract = False
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'


class Admin(ModelAdmin):
    icon = '<i class="material-icons">bookmark</i>'
    list_display = ('id', 'description', 'category', 'location')
