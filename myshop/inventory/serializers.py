from rest_framework import serializers
from .models import Product, Console, Accessory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ConsoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Console
        fields = '__all__'

class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'
