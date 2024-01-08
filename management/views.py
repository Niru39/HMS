from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Room, RoomType, EmployeeInfo
from rest_framework.response import Response
from .serializers import EmployeeInfoSerializier, RoomTypeSerializier, RoomSerializier
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class RoomView(ModelViewSet):  
    queryset = Room.objects.all()
    serializer_class = RoomSerializier
    
class RoomTypeView(ModelViewSet):  
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializier
    
class EmployeeInfoView(ModelViewSet):  
    queryset = EmployeeInfo.objects.all()
    serializer_class = EmployeeInfoSerializier


