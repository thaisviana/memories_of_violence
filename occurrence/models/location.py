from django.db import models
from django.contrib.admin import ModelAdmin, site


class Location(models.Model):
    locationName = models.TextField(null=False, blank=False, verbose_name='Nome da Localidade')
    lat = models.DecimalField(max_digits=16, decimal_places=8, null=False, blank=False, verbose_name='Latitute')
    lng = models.DecimalField(max_digits=16, decimal_places=8, null=False, blank=False, verbose_name='Longitude')

    def __str__(self):
        return self.locationName

    @classmethod
    def register_admin(cls):
        site.register(cls, Admin)

    class Meta:
        abstract = False
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'


class Admin(ModelAdmin):
    icon = '<i class="material-icons">photo_camera</i>'
    list_display = ('id', 'locationName',)
