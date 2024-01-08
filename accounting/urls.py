from django.urls import path
from .views import BillView, PaymentView

urlpatterns = [
#     path('bill/all/', bill_view, name = 'bill_list')
        path ('bill/all/',BillView.as_view({'get':'list','post':'create'}), name = 'bill-list'),
        path('bill/<int:pk>/', BillView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'bill-details'),
        path ('payment/all/',PaymentView.as_view({'get':'list','post':'create'}), name = 'payment-list'),
        path('payment/<int:pk>/', PaymentView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'payment-details')
]


