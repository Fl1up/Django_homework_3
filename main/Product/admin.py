from django.contrib import admin
from main.Product.models import Products, Category
from django import forms


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category','image')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

