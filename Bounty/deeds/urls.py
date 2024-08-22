from django.urls import path
from .views import create_deed, deed_list

urlpatterns = [
    path('create/', create_deed, name='create_deed'),
    path('list/', deed_list, name='deed_list'),
]
