from django.contrib import admin
from brands.models import *
from accounts.models import *
from brands.models import Group_models, User_django_models
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# apps inlines


class StoreInline(admin.StackedInline):
    model = Store
    extra = 1
    fields = (
        'id',
        'name',
        'address',
        'phone_number',
        'status',
        'country_code',
        'logo',
        'link_facebook',
        'link_youtube',
        'link_pinterest',
        'link_instagram',
        'web_site',
        'company',
        'inserted_at',
        'updated_at',)


class UserCompanyInline(admin.StackedInline):
    model = UserCompany
    fields = ('user',  'company', 'status', 'is_disabled',
              'inserted_at', 'updated_at'
              )
    extra = 1
    autocomplete_fields = ['user', 'company', ]

# Import-export class Company


class ContactResource(resources.ModelResource):
    class Meta:
        model = Company


@admin.register(Company)
class company_admin(ImportExportModelAdmin, admin.ModelAdmin):
    fields = [
        'name',
        'alias',
        'logo',
        'image_tag',
        'description',
        'inserted_at',
        'updated_at',
        'slug',
        'title',
        'cover_photo',
        'web_site',
    ]
    readonly_fields = ('image_tag',)

    list_display = (
        'id',
        'name',
        'alias',
        'logo',
        'image_tag',
        'description',
        'inserted_at',
        'updated_at',
        'slug',
        'title',
        'cover_photo',
        'web_site',
    )
    list_display_links = (
        'id', 'name',
    )
    search_fields = (
        'id', 'name', 'alias', 'title', 'web_site'
    )
    list_filter = (
        'inserted_at', 'updated_at',
    )

    inlines = [
        UserCompanyInline, StoreInline
    ]


admin.site.unregister(Group)
admin.site.register(Group_models, GroupAdmin)
admin.site.unregister(User)
admin.site.register(User_django_models, UserAdmin)
