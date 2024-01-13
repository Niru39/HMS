from rest_framework import serializers
from .models import Menu, Food

class MenuSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Menu
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = '__all__'

