from django.contrib import admin

from reservations.models import Reservation
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Reservation Admin"""
    pass