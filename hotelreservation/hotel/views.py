from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Hotel, Room, Guest, Reservation

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def room_list(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    return render(request, 'room_list.html', {'hotel': hotel, 'rooms': rooms})

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guest_list.html', {'guests': guests})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def create_reservation(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    if request.method == 'POST':
        # Handle form submission and create reservation
        pass
    return render(request, 'reservation_form.html', {'hotel': hotel, 'rooms': rooms})
