from django.db import models
from accounts.models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nombre',
                            help_text='Maximo de caracteres:50')
    alias = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name='Alias')
    logo = models.URLField(max_length=255, blank=True,
                           null=True, verbose_name='Logo')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descripcion',
                                   help_text='Maximo de caracteres:255')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    slug = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name='Titulo')
    cover_photo = models.TextField(
        blank=True, null=True, verbose_name='Imagen de compañia')
    web_site = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Sitio web')

    class Meta:
        managed = False
        db_table = 'company'
        verbose_name_plural = 'Compañias'

    def __str__(self):
        return self.name

    # Show image log from Company
    def image_tag(self):
        from django.utils.html import mark_safe
        if self.logo:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo))

        return mark_safe('<img src="https://lh3.googleusercontent.com/Iz_k_AtANBlGk49qRkXXTHvAF6UisUEU59nK69A0RB0KYymrO8j-Q6I5ZFUDc7z71fE" width="50" height="50"/>')
        image_tag.short_description = 'Image'


class Group_models(Group):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name_plural = ('Grupo')


class User_django_models(User):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = ('Super user')
