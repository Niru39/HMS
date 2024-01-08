from rest_framework import serializers
from .models import Room, RoomType, EmployeeInfo

class RoomSerializier(serializers.ModelSerializer):
    class Meta: 
        model = Room
        fields = '__all__'


class RoomTypeSerializier(serializers.ModelSerializer):
    class Meta: 
        model = RoomType
        fields = '__all__'

class EmployeeInfoSerializier(serializers.ModelSerializer):
    class Meta: 
        model = EmployeeInfo
        fields = '__all__'

