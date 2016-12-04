from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('category', 'name', 'price')


class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'products')
