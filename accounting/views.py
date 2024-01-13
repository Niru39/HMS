from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Bill, Payment
from rest_framework.response import Response
from .serializers import BillSerializer, PaymentSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

# @api_view(['GET']) # to define request nature
# def bill_view(request):
#     bill_obj = Bill.objects.all()
#     bill_json = BillSerializier(bill_obj, many = True) # to change object data into json data
    
#     return Response(bill_json.data)


#  to make class base view we can define multiple methods, class le request ledaina

class BillView(ModelViewSet):  # inherit
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def list(self, request): # to get selective data from the bill eg: without null
        queryset = self.get_queryset() 
        serializer = self.serializer_class(queryset, many = True) # querystele objects data nae dinxa
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data) # datale jsondata lai object data ma change garxa
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def retrieve(self, request , pk = None):
        try:
            queryset = Bill.objects.get(id = pk) # to retrieve only one value
        except:
            return Response({'error':'Not Found'})
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk = None):
        try:
            queryset = Bill.objects.get(id = pk) 
        except:
            return Response({'error':'Not Found'})
        serializer = self.serializer_class(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def destroy(self, request, pk = None):
        try:
            queryset = Bill.objects.get(id = pk) # to retrieve only one value
        except:
            return Response({'error':'Not Found'})
        queryset.delete()
        return Response('Data Deleted.')
    
    
class PaymentView(ModelViewSet):  # inherit
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer