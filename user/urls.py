from .views import login, owner_create
from django.urls import path

urlpatterns = [
    path('login/',login, name = 'login'),
    path('owner_create/', owner_create, name = 'owner_create')
]
