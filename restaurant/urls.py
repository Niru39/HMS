from django.urls import path
from .views import MenuView, FoodView

urlpatterns = [

        path ('menu/all/',MenuView.as_view({'get':'list','post':'create'}), name = 'menu-list'),
        path('menu/<int:pk>/', MenuView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'menu-details'),
        path ('food/all/',FoodView.as_view({'get':'list','post':'create'}), name = 'food-list'),
        path('food/<int:pk>/', FoodView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'food-details')
]

