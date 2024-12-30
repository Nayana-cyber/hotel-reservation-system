from django.contrib import admin
from .models import Hotel, Room, Guest, Reservation

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
