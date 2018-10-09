from django.db import models
from django.contrib.admin import ModelAdmin, site


class Asset(models.Model):
    IMAGE = 'IM'
    VIDEO = 'VI'
    TYPE_CHOICES = (
        (IMAGE, 'Imagem'),
        (VIDEO, 'Vídeo'),)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=IMAGE,)
    hashId = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    occurrence = models.ForeignKey('occurrence.Occurrence', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} , {}".format(self.get_type_display(), self.url)

    @classmethod
    def register_admin(cls):
        site.register(cls, Admin)

    class Meta:
        abstract = False
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'


class Admin(ModelAdmin):
    icon = '<i class="material-icons">bookmark</i>'
    list_display = ('type', 'url',)
