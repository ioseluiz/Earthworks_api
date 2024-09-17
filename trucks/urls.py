from django.urls import path

from .views import truck_list, truck_details

urlpatterns = [
    path('', truck_list, name='truck-list'),
    path('<int:pk>', truck_details, name='truck-details'),
]