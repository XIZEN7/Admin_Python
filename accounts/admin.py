from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Import-export class User


class UserResource(resources.ModelResource):
    class Meta:
        model = User

# user admin


@admin.register(User)
class User_profile_admin(ImportExportModelAdmin, admin.ModelAdmin):
    fields = (
        'name',
        'last_name',
        'email',
        'country_code',
        'phone_number',
        'picture',
        'status',
        'os',
    )
    list_display = (
        'id',
        'name',
        'last_name',
        'email',
        'country_code',
        'phone_number',
        'picture',
        'status',
        'os',
        'validation_code',
        'code_validated_at',
        'activated_keyboard',
        'first_use',
        'inserted_at',
        'updated_at',
    )
    list_display_links = (
        'id', 'phone_number', 'email',
    )
    search_fields = ['id', 'name', 'email',
                     'phone_number', 'code_validated_at']
    list_filter = (
        'inserted_at', 'updated_at', 'os', 'status', 'activated_keyboard', 'first_use',
    )


# Import-export class UserCompany
class UserCompanyResource(resources.ModelResource):
    class Meta:
        model = UserCompany

# user_company admin


@admin.register(UserCompany)
class user_company_admin(ImportExportModelAdmin, admin.ModelAdmin):
    fields = ('user', 'company', 'status', 'is_disabled',)
    list_display = ('user', 'company', 'Email', 'Telefono',
                    'status', 'inserted_at', 'updated_at', 'is_disabled', )
    search_fields = ('user__name', 'company__name',
                     'user__phone_number', 'user__email')
    list_filter = ('inserted_at', 'updated_at', 'status', 'is_disabled', )
    autocomplete_fields = ['user', 'company', ]

    def Email(self, obj):
        return obj.user.email

    def Telefono(self, obj):
        return obj.user.phone_number
# Import-export class UserStore


class UserStoreResource(resources.ModelResource):
    class Meta:
        model = UserStore

# user_store


@admin.register(UserStore)
class user_store_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'store', 'status',
                    'inserted_at', 'updated_at')
    search_fields = ('id', 'user__name', 'store__name',)
    list_display_links = ('id', 'user',)
    list_filter = ('status', 'inserted_at', 'updated_at')

# Import-export class Contact


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

# contact


@admin.register(Contact)
class contact_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'country_code',
        'phone_number',
        'user_facebook',
        'user_instagram',
        'facebook_url',
        'address',
        'description',
        'store',
        'inserted_at',
        'updated_at',
        'address_add_on',
    )
    search_fields = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'user_facebook',
        'user_instagram',
        'store__name',
    )
    list_display_links = (
        'id', 'first_name', 'last_name', 'email', 'phone_number', 'user_facebook', 'user_instagram',
    )
    list_filter = (
        'is_disabled', 'status', 'inserted_at', 'updated_at', 'address_add_on', 'country_code', 'address_add_on',
    )

# Import-export class ContactStatus


class ContactStatusResource(resources.ModelResource):
    class Meta:
        model = ContactStatus


@admin.register(ContactStatus)
class contact_status_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'name', 'company', 'color', 'inserted_at', 'updated_at'
    )
    search_fields = (
        'id', 'name', 'company__name',
    )
    list_display_links = (
        'id', 'name',
    )
    list_filter = (
        'inserted_at', 'updated_at'
    )

    class Meta:
        app_label = 'Contact Status'

# Import-export class Session


"""
class SessionResource(resources.ModelResource):
    class Meta:
        model = Session


@admin.register(Session)
class session_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'Email',
        'Telefono',
        'application',
        'version',
        'os',
        'status',
        'device_id',
        'device_brand',
        'device_model',
        'device_version',
        'inserted_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'user__name',
        'user__phone_number',
        'user__email',
        'token',
        'firebase_token',
        'device_id',
        'device_brand',
        'device_model',
        'device_version'
    )
    list_display_links = (
        'id', 'user', 'device_id',
    )
    list_filter = (
        'inserted_at', 'updated_at', 'status', 'os',
    )

    def Email(self, obj):
        return obj.user.email

    def Telefono(self, obj):
        return obj.user.phone_number
# Import-export class Message


class MessageResource(resources.ModelResource):
    class Meta:
        model = Message
"""


@admin.register(Message)
class message_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'body',
        'store',
        'message_category',
        'company',
        'inserted_at',
        'updated_at',
        'owner',
    )
    search_fields = (
        'id', 'name', 'company__name', 'store__name', 'owner',
    )
    list_display_links = (
        'id', 'name',
    )
    list_filter = (
        'inserted_at', 'updated_at'
    )

# Import-export class MessageCategory


class MessageCategoryResource(resources.ModelResource):
    class Meta:
        model = MessageCategory


@admin.register(MessageCategory)
class message_category_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'name', 'store', 'company', 'inserted_at', 'inserted_at', 'owner',
    )
    search_fields = (
        'id', 'name', 'store__name', 'company__name'
    )
    list_display_links = (
        'id', 'name',
    )
    list_filter = (
        'inserted_at', 'updated_at'
    )
