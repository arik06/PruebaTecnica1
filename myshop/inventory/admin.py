from django.contrib import admin
from .models import Product, Console, Accessory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)

@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'created_at')
    search_fields = ('name', 'type')

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)
