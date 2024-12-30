from django.urls import path
from .views import hotel_list, room_list, guest_list, reservation_list, create_reservation

urlpatterns = [
    path('', hotel_list, name='hotel_list'),
    path('hotel/<int:hotel_id>/rooms/', room_list, name='room_list'),
    path('guests/', guest_list, name='guest_list'),
    path('reservations/', reservation_list, name='reservation_list'),
    path('hotel/<int:hotel_id>/reserve/', create_reservation, name='create_reservation'),
]
