from django.contrib import admin
from store.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class StoreResource(resources.ModelResource):
    class Meta:
        model = Store


@admin.register(Store)
class store_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'address',
        'phone_number',
        'status',
        'country_code',
        'logo',
        'image_tag',
        'link_facebook',
        'link_youtube',
        'link_pinterest',
        'link_instagram',
        'web_site',
        'company',
        'inserted_at',
        'updated_at',
    )
    list_display_links = (
        'id', 'name', 'phone_number',
    )
    search_fields = [
        'id',
        'name',
        'phone_number',
        'link_facebook',
        'link_youtube',
        'link_pinterest',
        'link_instagram',
        'web_site',
        'company__name',
    ]
    list_filter = (
        'inserted_at', 'updated_at', 'status'
    )

    resource_class = StoreResource
