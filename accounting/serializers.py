from rest_framework import serializers 
from .models import  Bill, Payment
 # serialzier is used to change the datatype and querystes ino json format, backend le frontendlai data api through pathaune serialzier 
 #use hunxa and vice versa, serializier le frontend bata pathako json data lai objectsma convert garera database ma save garxa
 
class BillSerializier(serializers.ModelSerializer):
    class Meta: #meta has  extrafeatures of defined class serializier
        model = Bill
        fields = '__all__'


class PaymentSerializier(serializers.ModelSerializer):
    class Meta: 
        model = Payment
        fields = '__all__'
