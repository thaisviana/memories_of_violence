from django.db import models


class Location(models.Model):
    locationName = models.TextField(null=False, blank=False, verbose_name='Nome da Localidade')
    lat = models.DecimalField(max_digits=16, decimal_places=8, null=False, blank=False, verbose_name='Latitute')
    lng = models.DecimalField(max_digits=16, decimal_places=8, null=False, blank=False, verbose_name='Longitude')

    def __str__(self):
        return self.locationName

    class Meta:
        abstract = False