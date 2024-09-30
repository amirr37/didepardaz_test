from rest_framework import serializers
from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = Brand
        fields = ['id', 'title', 'country']
