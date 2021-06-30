from django.db import models
from brands.models import *

# Create your models here.


class Store(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nombre',
                            help_text='Maximo de caracteres:50')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Direccion',
                               help_text='Maximo de caracteres:255')
    phone_number = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='Numero de telefono')
    status = models.BooleanField(blank=True, null=True, verbose_name='Estado')
    country_code = models.CharField(
        max_length=10, blank=True, null=True, verbose_name='Codigo de pais')
    logo = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Logo')
    link_facebook = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Link Facebook')
    link_youtube = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Link Youtube')
    link_pinterest = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Link Pinterest')
    link_instagram = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Link Instagram')
    web_site = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Sitio web')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True, verbose_name='Campañia')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)

    class Meta:
        managed = False
        db_table = 'store'
        verbose_name_plural = 'Tiendas'

    def __str__(self):
        return self.name

    # Show image logo from store
    def image_tag(self):
        from django.utils.html import mark_safe
        if self.logo:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo))
        return mark_safe(
            '<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fareajugones.sport.es%2Fvideojuegos%2Fpokemon-espada-y-escudo-como-capturar-a-charmander%2F&psig=AOvVaw1es5wn8PuSDNz-oL0R1E74&ust=1618718143693000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDR5ZixhPACFQAAAAAdAAAAABAF" width="50" height="50"/>')
        image_tag.short_description = 'Image'
