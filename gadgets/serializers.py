from unicodedata import category
from rest_framework import serializers
from .models import Product, Tag, ProductCategory
from importlib.resources import read_binary

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'id',)

class ProductWritableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('tags',)



class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price','tags')

class ProductCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'
