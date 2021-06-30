from django.db import models
from brands.models import *
from store.models import *
from django.utils import timezone
from store.models import *


class AdminSharingHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_sharing_history'


class ColorStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'color_status'

    def __str__(self):
        return self.color


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Nombre')
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Apellido')
    email = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name='Correo electronico')
    phone_number = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='Numero de telefono')
    user_facebook = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Usuario de Facebook')
    user_instagram = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Usuario de Instagram')
    facebook_url = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Facebook Url')
    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Direccion')
    description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Decripcion')
    is_disabled = models.BooleanField(verbose_name='Deshabilitado')
    store = models.ForeignKey(Store, models.DO_NOTHING, verbose_name='Tienda')
    status = models.ForeignKey(
        'ContactStatus', models.DO_NOTHING, verbose_name='Estado')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    country_code = models.CharField(
        max_length=5, blank=True, null=True, verbose_name='Codigo de pais')
    address_add_on = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Direccion agregada en')

    class Meta:
        managed = False
        db_table = 'contact'
        verbose_name_plural = 'Contacto'


class ContactStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Nombre')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, verbose_name='Compañia')
    color = models.ForeignKey(
        ColorStatus, models.DO_NOTHING, verbose_name='Color')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)

    class Meta:
        managed = False
        db_table = 'contact_status'
        verbose_name_plural = 'Estado del contacto'

    def __str__(self):
        return self.name


class GuardianTokens(models.Model):
    jti = models.CharField(primary_key=True, max_length=255)
    aud = models.CharField(max_length=255)
    typ = models.CharField(max_length=255, blank=True, null=True)
    iss = models.CharField(max_length=255, blank=True, null=True)
    sub = models.CharField(max_length=255, blank=True, null=True)
    exp = models.BigIntegerField(blank=True, null=True)
    jwt = models.TextField(blank=True, null=True)
    # This field type is a guess.
    claims = models.TextField(blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'guardian_tokens'
        unique_together = (('jti', 'aud'),)


class Indicator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'indicator'
        unique_together = (('company', 'name'),)


class IndicatorSharingHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.IntegerField(blank=True, null=True)
    indicator = models.ForeignKey(
        Indicator, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'indicator_sharing_history'


class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Nombre')
    body = models.TextField(blank=True, null=True, verbose_name='Cuerpo')
    store = models.ForeignKey(Store, models.DO_NOTHING,
                              blank=True, null=True, verbose_name='Tienda')
    message_category = models.ForeignKey(
        'MessageCategory', models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria de mensaje')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True, verbose_name='Compañia')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    owner = models.CharField(max_length=255, verbose_name='Propietario')

    class Meta:
        managed = False
        db_table = 'message'
        unique_together = (('name', 'company'),)
        verbose_name_plural = 'Mensajes'


class MessageCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Nombre')
    store = models.ForeignKey(Store, models.DO_NOTHING,
                              blank=True, null=True, verbose_name='Tienda')
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True, verbose_name='Compañia')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    owner = models.CharField(max_length=255, verbose_name='Propietario')

    class Meta:
        managed = False
        db_table = 'message_category'
        unique_together = (('name', 'company'),)
        verbose_name_plural = 'Categoria del mensaje'

    def __str__(self):
        return self.name


class NotificationOpting(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    status = models.BooleanField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notification_opting'
        unique_together = (('user', 'type'),)


class Pqr(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pqr'


class SchemaMigrations(models.Model):
    version = models.BigIntegerField(primary_key=True)
    inserted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Session(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True,
                          null=True, verbose_name='OS')
    status = models.BooleanField(blank=True, null=True, verbose_name='Estado')
    token = models.TextField(blank=True, null=True, verbose_name='Token')
    firebase_token = models.TextField(
        blank=True, null=True, verbose_name='Token Firebase')
    device_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Id Dispositivo')
    device_brand = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Marca de Dispositivo')
    device_model = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Modelo de Dispositivo')
    device_version = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Version de Dispositivo')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)

    class Meta:
        managed = False
        db_table = 'session'
        verbose_name_plural = 'Sesiones'


class SharingInfoContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=360, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    so = models.CharField(max_length=255, blank=True, null=True)
    entity_id = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING)
    contact = models.ForeignKey(
        Contact, models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category_name = models.CharField(max_length=255, null=True)

    class Meta:
        managed = False
        db_table = 'sharing_info_contact'


class Shortcut(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shortcut'
        unique_together = (('type', 'name', 'company'),)


class ShortcutApp(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    android_url = models.CharField(max_length=255, blank=True, null=True)
    ios_url = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(
        Company, models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shortcut_app'
        unique_together = (('name', 'company'),)


class ShortcutMail(models.Model):
    id = models.BigAutoField(primary_key=True)
    destinatary = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shortcut_mail'


class ShortcutWeb(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shortcut_web'

    def __str__(self):
        return self.name


class TempMultimedia(models.Model):
    uri = models.TextField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    entity_type = models.TextField(blank=True, null=True)
    sku = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_multimedia'


class TempProduct(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    reference_code = models.TextField(blank=True, null=True)
    categoria3 = models.TextField(blank=True, null=True)
    idzona = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_product'


class TemporalProductDetails(models.Model):
    price = models.FloatField(blank=True, null=True)
    sku = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporal_product_details'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nombre',
                            help_text='Maximo de caracteres: 50')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Apellido',
                                 help_text='Maximo de caracteres:50')
    email = models.EmailField(unique=True, max_length=100,
                              blank=True, null=True, verbose_name='Correo electronico')
    country_code = models.CharField(
        max_length=10, blank=True, null=True, verbose_name='Codigo pais')
    phone_number = models.CharField(
        unique=True, max_length=11, blank=True, null=True, verbose_name='Numero de telefono')
    password = models.TextField(
        blank=True, null=True, verbose_name='Contraseña')
    picture = models.TextField(blank=True, null=True, verbose_name='Imagen')
    status = models.BooleanField(blank=True, null=True, verbose_name='Estado')
    os = models.CharField(max_length=255, blank=True,
                          null=True, verbose_name='OS')
    validation_code = models.TextField(
        blank=True, null=True, verbose_name='Codigo de validacion')
    code_validated_at = models.DateTimeField(
        blank=True, null=True, verbose_name='Codigo validado en')
    activated_keyboard = models.BooleanField(
        blank=True, null=True, verbose_name='Teclado activado')
    first_use = models.BooleanField(
        blank=True, null=True, verbose_name='Primer uso')
    inserted_at = models.DateTimeField(
        verbose_name='Ingresado en', blank=True, null=True)
    updated_at = models.DateTimeField(
        verbose_name='Actualizado en', null=True,)

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name_plural = 'Usuarios'

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.inserted_at = timezone.now()
        self.updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserCompany(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, related_name='sellers', on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='Compañia')
    status = models.BooleanField(blank=True, null=True, verbose_name='Estado')
    inserted_at = models.DateTimeField(
        verbose_name='Ingresado en', blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)
    is_disabled = models.BooleanField(
        blank=True, null=True, verbose_name='Deshabilitado')

    class Meta:
        managed = False
        db_table = 'user_company'

        verbose_name_plural = 'Usuario en compañia'

    def __str__(self):
        return self.user.name


class UserStore(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING,
                              blank=True, null=True, verbose_name='Tienda')
    status = models.BooleanField(blank=True, null=True, verbose_name='Estado')
    inserted_at = models.DateTimeField(verbose_name='Ingresado en', null=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado en', null=True)

    class Meta:
        managed = False
        db_table = 'user_store'
        verbose_name_plural = 'Usuario en tienda'
