from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'date_time', 'price', 'image']
    list_display_links = ['id', 'title']
    list_filter = ['category']
    search_fields = ['title', 'description']
    readonly_fields = ['date_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']
