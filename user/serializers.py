from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
class UserSerializier(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['email', 'password']
        
class GroupSerializier(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']