from django.contrib import admin
from .models import (
    Product, Category, SeasonalEvents, ProductType, Attribute, AttributeValue,
    ProductLine, productImage, ProductLine_AttributeValue, Product_ProductType, StockControl
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pid', 'name', 'slug', 'category', 'seasonal_events', 'description',
        'is_digtial', 'created_at', 'updated_at', 'is_active', 'stock_status'
    )
    list_filter = ('category', 'seasonal_events', 'is_digtial', 'is_active', 'stock_status')
    search_fields = ('name', 'slug', 'description')
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'parent_category')
    list_filter = ('is_active', 'parent_category')
    search_fields = ('name', 'slug')
    ordering = ('name',)

@admin.register(SeasonalEvents)
class SeasonalEventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name',)
    ordering = ('start_date',)

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute_value', 'attribute')
    list_filter = ('attribute',)
    search_fields = ('attribute_value',)
    ordering = ('attribute_value',)

@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    list_display = ('price', 'sku', 'product', 'stock_qty', 'is_active', 'order', 'weight')
    list_filter = ('product', 'is_active')
    search_fields = ('sku', 'product__name')
    ordering = ('order',)

@admin.register(productImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_line', 'alternative_text', 'url', 'order')
    list_filter = ('product_line',)
    search_fields = ('name', 'alternative_text')
    ordering = ('order',)

@admin.register(ProductLine_AttributeValue)
class ProductLine_AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute_value', 'product_line')
    list_filter = ('attribute_value', 'product_line')
    search_fields = ('attribute_value__attribute_value', 'product_line__sku')

@admin.register(Product_ProductType)
class Product_ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_type')
    list_filter = ('product', 'product_type')
    search_fields = ('product__name', 'product_type__name')

@admin.register(StockControl)
class StockControlAdmin(admin.ModelAdmin):
    list_display = ('stock_qty', 'name', 'stock_product')
    list_filter = ('stock_product',)
    search_fields = ('name', 'stock_product__name')
    ordering = ('name',)
