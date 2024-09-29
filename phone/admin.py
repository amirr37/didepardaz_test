from django.contrib import admin
from phone.models import Country, Phone, Brand


# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'country']


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['model', 'price', 'color', 'screen_size', 'in_stock', 'origin_country']
    list_filter = ['model', 'price', 'color', 'screen_size', 'in_stock']
    list_editable = ['price', 'in_stock']

