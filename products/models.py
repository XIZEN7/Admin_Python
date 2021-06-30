from django.db import models
from brands.models import *
from store.models import *

# Create your models here.


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Nombre')
    description = models.TextField(
        blank=True, null=True, verbose_name='Descripcion')
    reference_code = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Codigo de referencia')
    alias = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name='Alias')
    product_category = models.ForeignKey(
        'ProductCategory', models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria de producto')
    store = models.ForeignKey(Store, models.DO_NOTHING,
                              blank=True, null=True, verbose_name='Tienda')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True, verbose_name='Compañia')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    owner = models.CharField(max_length=255, verbose_name='Propietario')

    class Meta:
        managed = False
        db_table = 'product'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Nombre')
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True, verbose_name='Nivel')
    store = models.ForeignKey(Store, models.DO_NOTHING,
                              blank=True, null=True, verbose_name='Tienda')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True, verbose_name='Compañia')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    owner = models.CharField(max_length=255, verbose_name='Propietario')

    class Meta:
        managed = False
        db_table = 'product_category'
        unique_together = (('name', 'level', 'parent_id', 'company'),)
        verbose_name_plural = 'Categoria de producto'

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    validity = models.BooleanField(
        blank=True, null=True, verbose_name='Validez')
    visibility = models.BooleanField(
        blank=True, null=True, verbose_name='Visibilidad')
    link_visibility = models.BooleanField(
        blank=True, null=True, verbose_name='Visibilidad de link')
    price = models.FloatField(blank=True, null=True, verbose_name='Precio')
    currency = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Moneda')
    product = models.ForeignKey(
        Product, models.DO_NOTHING, blank=True, null=True, verbose_name='Producto')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    reference_code = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Codigo de referencia')

    class Meta:
        managed = False
        db_table = 'product_details'
        verbose_name_plural = 'Detalles de producto'


class ProductValidity(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.FloatField(blank=True, null=True, verbose_name='Precio')
    currency = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Moneda')
    name = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Nombre')
    validity_start_date = models.DateTimeField(
        blank=True, null=True, verbose_name='Fecha inicial de validez')
    validity_end_date = models.DateTimeField(
        blank=True, null=True, verbose_name='Fecha final de validez')
    product = models.ForeignKey(
        Product, models.DO_NOTHING, blank=True, null=True, verbose_name='Producto')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)

    class Meta:
        managed = False
        db_table = 'product_validity'
        verbose_name_plural = 'Validez de producto'
