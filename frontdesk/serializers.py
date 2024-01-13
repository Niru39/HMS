from rest_framework import serializers 
from .models import  GuestInfo, GuestRoom
 # serialzier is used to change the datatype and querystes ino json format, backend le frontendlai data api through pathaune serialzier 
 #use hunxa and vice versa, serializier le frontend bata pathako json data lai objectsma convert garera database ma save garxa
 
class GuestInfoSerializer(serializers.ModelSerializer):
    class Meta: #meta has  extrafeatures of defined class serializier
        model = GuestInfo
        fields = '__all__'


class GuestRoomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = GuestRoom
        fields = '__all__'
