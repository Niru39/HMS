from django.urls import path
from .views import GuestInfoView, GuestRoomView

urlpatterns = [

        path ('guestinfo/all/',GuestInfoView.as_view({'get':'list','post':'create'}), name = 'guestinfo-list'),
        path('guestinfo/<int:pk>/', GuestInfoView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'guestinfo-details'),
        path ('guestroom/all/',GuestRoomView.as_view({'get':'list','post':'create'}), name = 'guestroom-list'),
        path('guestroom/<int:pk>/', GuestRoomView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'guestroom-details')
]

