from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Room, RoomType, EmployeeInfo
from rest_framework.response import Response
from .serializers import EmployeeInfoSerializier, RoomTypeSerializier, RoomSerializier
from rest_framework.viewsets import ModelViewSet
from user.serializers import UserSerializier
from user.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

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
    
    def create(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        group_id = request.data.get('group')
        group_obj = Group.objects.get(id = group_id)
        hash_password = make_password(password)
        serializier = UserSerializier(data = request.data)
        if serializier.is_valid():
            serializier = self.serializer_class(data = request.data)
            if serializier.is_valid():
                user = User.objects.create(email = email, password = hash_password)
                a = serializier.save()
                a.user = user
                a.save()
                return Response(serializier.data)
            else:
                return Response(serializier.errors)
        else:
            return Response(serializier.errors)

