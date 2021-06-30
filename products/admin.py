from django.contrib import admin
from products.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Import-export class Product


class ProducttResource(resources.ModelResource):
    class Meta:
        model = Product


@admin.register(Product)
class product_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'reference_code',
        'alias',
        'product_category',
        'store',
        'company',
        'inserted_at',
        'updated_at',
        'owner',
    )
    list_display_links = ('id', 'name', )
    search_fields = [
        'id',
        'name',
        'reference_code',
        'store__name',
        'company__name',
        'owner',
    ]
    list_filter = ('inserted_at', 'updated_at',)

# Import-export class ProductCategory


class ProductCategoryResource(resources.ModelResource):
    class Meta:
        model = ProductCategory


@admin.register(ProductCategory)
class product_category_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'parent_id',
        'level',
        'store',
        'company',
        'inserted_at',
        'updated_at',
        'owner',
    )
    list_display_links = ('id', 'name', )
    search_fields = [
        'id',
        'name',
        'parent_id',
        'level',
        'company__name',
        'owner',
    ]
    list_filter = ('inserted_at', 'updated_at', 'company',)

# Import-export class ProductDetails


class ProductDetailsResource(resources.ModelResource):
    class Meta:
        model = ProductDetails


@admin.register(ProductDetails)
class product_details_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'validity',
        'visibility',
        'link_visibility',
        'price',
        'currency',
        'product',
        'inserted_at',
        'updated_at',
        'reference_code',
    )
    list_display_links = ('id', )
    search_fields = [
        'id', 'product__name', 'price',
    ]
    list_filter = ('inserted_at', 'updated_at', 'validity', 'visibility', 'link_visibility',
                   'currency',
                   )

# Import-export class ProductValidity


class ProductValidityResource(resources.ModelResource):
    class Meta:
        model = ProductValidity


@admin.register(ProductValidity)
class product_validity_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'price',
        'name',
        'validity_start_date',
        'validity_end_date',
        'product',
        'inserted_at',
        'updated_at',

    )
    list_display_links = ('id', 'product', 'name', )
    search_fields = [
        'id', 'product__name', 'name',
    ]
    list_filter = ('inserted_at', 'updated_at', )
