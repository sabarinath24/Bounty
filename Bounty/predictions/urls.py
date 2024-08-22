from django.urls import path
from .views import create_prediction, prediction_list

urlpatterns = [
    path('create/', create_prediction, name='create_prediction'),
    path('list/', prediction_list, name='prediction_list'),
]
