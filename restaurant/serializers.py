from rest_framework import serializers
from .models import Menu, Food

class MenuSerializier(serializers.ModelSerializer):
    class Meta: 
        model = Menu
        fields = '__all__'


class FoodSerializier(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = '__all__'

