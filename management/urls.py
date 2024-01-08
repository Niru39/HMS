from django.urls import path
from .views import RoomView, RoomTypeView, EmployeeInfoView

urlpatterns = [

        path ('room/all/',RoomView.as_view({'get':'list','post':'create'}), name = 'room-list'),
        path('room/<int:pk>/', RoomView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'room-details'),
        path ('roomtype/all/',RoomTypeView.as_view({'get':'list','post':'create'}), name = 'roomtype-list'),
        path('roomtype/<int:pk>/', RoomTypeView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'roomtype-details'),
        path ('employeeinfo/all/',EmployeeInfoView.as_view({'get':'list','post':'create'}), name = 'employeeinfo-list'),
        path('employeeinfo/<int:pk>/', EmployeeInfoView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'employeeinfo-details')
]

