from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    title = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Country')

    def __str__(self):
        return self.title


class Phone(models.Model):
    model = models.CharField(max_length=100, unique=True, verbose_name='phone Model')
    price = models.PositiveIntegerField(validators=[MinValueValidator(1), ], verbose_name='Price')
    color = models.CharField(max_length=100, verbose_name='Color')
    screen_size = models.PositiveIntegerField(validators=[MinValueValidator(1), ], verbose_name='Screen Size')
    in_stock = models.BooleanField(default=True, verbose_name='In Stock')
    origin_country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Origin Country')

    def __str__(self):
        return self.model

