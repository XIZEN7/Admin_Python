from django.contrib import admin
from multimedia.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# Import-export class File


class FileResource(resources.ModelResource):
    class Meta:
        model = File


@admin.register(File)
class file_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'shareable',
        'validity',
        'store',
        'company',
        'file_category',
        'owner',
    )
    list_display_links = (
        'id', 'name', 'store', 'company', 'owner',
    )
    search_fields = (
        'id', 'name',
    )
    list_filter = (
        'inserted_at', 'updated_at', 'shareable', 'validity',
    )

# Import-export class FileCategory


class FileCategoryResource(resources.ModelResource):
    class Meta:
        model = FileCategory


@admin.register(FileCategory)
class file_category_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'name', 'store', 'company', 'owner',  'inserted_at', 'updated_at',
    )
    list_display_links = (
        'id',  'name',
    )
    search_fields = (
        'id', 'name', 'store__name', 'company__name', 'owner',
    )
    list_filter = (
        'inserted_at', 'updated_at',
    )

# Import-export class FileValidity


class FileValidityResource(resources.ModelResource):
    class Meta:
        model = FileValidity


@admin.register(FileValidity)
class file_validity_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'validity_start_date', 'validity_end_date', 'file', 'inserted_at', 'updated_at',
    )
    list_display_links = (
        'id',
    )
    search_fields = (
        'id', 'file',
    )
    list_filter = (
        'inserted_at', 'updated_at',
    )

# Import-export class Multimedia


class MultimediaResource(resources.ModelResource):
    class Meta:
        model = Multimedia


@admin.register(Multimedia)
class multimedia_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'uri', 'type', 'size', 'entity_id', 'entity_type',
    )
    list_display_links = (
        'id',
    )
    search_fields = (
        'id', 'uri', 'type', 'entity_id',
    )
    list_filter = (
        'entity_type', 'type',
    )
