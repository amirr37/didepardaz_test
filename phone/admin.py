from django.contrib import admin
from phone.models import Country, Phone, Brand


# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass
