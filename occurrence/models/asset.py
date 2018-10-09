from django.db import models


class Asset(models.Model):
    IMAGE = 'IM'
    VIDEO = 'VI'
    TYPE_CHOICES = (
        (IMAGE, 'Imagem'),
        (VIDEO, 'Vídeo'),)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=IMAGE,)
    hashId = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.get_type_display(), self.url

    class Meta:
        abstract = False