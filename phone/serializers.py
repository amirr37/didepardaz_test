from rest_framework import serializers
from .models import Brand, Phone


class BrandSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = Brand
        fields = ['id', 'title', 'country']


class PhoneSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()  # Display brand title
    origin_country = serializers.StringRelatedField()  # Display origin country name
    brand_country = serializers.StringRelatedField(source='brand.country')  # Display brand's country name

    class Meta:
        model = Phone
        fields = ['id', 'model', 'brand', 'origin_country', 'brand_country']

