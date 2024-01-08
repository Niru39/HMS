from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import GuestInfo, GuestRoom
from rest_framework.response import Response
from .serializers import GuestInfoSerializier, GuestRoomSerializier
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class GuestInfoView(ModelViewSet):  # inherit
    queryset = GuestInfo.objects.all()
    serializer_class = GuestInfoSerializier
    
class GuestRoomView(ModelViewSet):  # inherit
    queryset = GuestRoom.objects.all()
    serializer_class = GuestRoomSerializier
