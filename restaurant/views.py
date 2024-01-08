from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, Food
from rest_framework.response import Response
from .serializers import MenuSerializier, FoodSerializier
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class MenuView(ModelViewSet):  
    queryset = Menu.objects.all()
    serializer_class = MenuSerializier
    
class FoodView(ModelViewSet):  
    queryset = Food.objects.all()
    serializer_class = FoodSerializier

