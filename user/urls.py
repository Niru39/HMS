from .views import login, owner_create, grouplist
from django.urls import path

urlpatterns = [
    path('login/',login, name = 'login'),
    path('grouplist/',grouplist, name = 'grouplist'),
    path('owner_create/', owner_create, name = 'owner_create')
]
