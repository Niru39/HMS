from rest_framework import serializers
from .models import Room, RoomType, EmployeeInfo

class RoomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Room
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RoomType
        fields = '__all__'

class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EmployeeInfo
        fields = '__all__'

