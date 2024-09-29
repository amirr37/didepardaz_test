from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


# todo : update database and remove null created and updated at

class Country(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Brand(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Country')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at', null=True, blank=True)

    def __str__(self):
        return self.title


class Phone(models.Model):
    model = models.CharField(max_length=100, unique=True, verbose_name='phone Model', db_index=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Brand', related_name='phones', null=True,
                              blank=True)  # todo : remnvoe null blank
    price = models.PositiveIntegerField(validators=[MinValueValidator(1), ], verbose_name='Price', db_index=True)
    color = models.CharField(max_length=100, verbose_name='Color')
    screen_size = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name='Screen Size'
    )
    in_stock = models.BooleanField(default=True, verbose_name='In Stock')
    origin_country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Origin Country',
                                       db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at', null=True, blank=True)

    def __str__(self):
        return self.model
