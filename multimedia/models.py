from django.db import models
from brands.models import *
from store.models import *

# Create your models here.


class File(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Nombre')
    description = models.TextField(
        blank=True, null=True, verbose_name='Descripcion')
    shareable = models.BooleanField(blank=True, null=True)
    validity = models.BooleanField(
        blank=True, null=True, verbose_name='Validez')
    store = models.ForeignKey(Store, models.DO_NOTHING,
                              blank=True, null=True, verbose_name='Tienda')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True, verbose_name='Compañia')
    file_category = models.ForeignKey(
        'FileCategory', models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria de archivo')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en')
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    owner = models.CharField(max_length=255, verbose_name='Propietario')

    class Meta:
        managed = False
        db_table = 'file'
        unique_together = (('name', 'company'),)
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return self.name


class FileCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Nombre')
    store = models.ForeignKey(Store, models.DO_NOTHING,
                              blank=True, null=True, verbose_name='Tienda')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True, verbose_name='Compañia')
    inserted_at = models.DateTimeField(verbose_name='Insertado en')
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    owner = models.CharField(max_length=255, verbose_name='Propietario')

    class Meta:
        managed = False
        db_table = 'file_category'
        unique_together = (('name', 'company'),)
        verbose_name_plural = 'Categoria de archivos'

    def __str__(self):
        return self.name


class FileValidity(models.Model):
    id = models.BigAutoField(primary_key=True)
    validity_start_date = models.DateTimeField(
        blank=True, null=True, verbose_name='Fecha inicial de validez')
    validity_end_date = models.DateTimeField(
        blank=True, null=True, verbose_name='Fecha final de validez')
    file = models.ForeignKey(File, models.DO_NOTHING,
                             blank=True, null=True, verbose_name='Archivo')
    inserted_at = models.DateTimeField(verbose_name='Insertado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)

    class Meta:
        managed = False
        db_table = 'file_validity'
        verbose_name_plural = 'Validacion de archivo'


class Multimedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    uri = models.URLField(max_length=255, blank=True,
                          null=True, verbose_name='Uri')
    type = models.IntegerField(blank=True, null=True, verbose_name='Tipo')
    size = models.IntegerField(blank=True, null=True, verbose_name='Tamaño')
    entity_id = models.IntegerField(
        blank=True, null=True, verbose_name='Id de entidad')
    entity_type = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Tipo de entidad')

    class Meta:
        managed = False
        db_table = 'multimedia'
        verbose_name_plural = 'Multimedia'
