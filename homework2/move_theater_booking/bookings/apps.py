from django.apps import AppConfig


class BookingsConfig(AppConfig):
    name = 'bookings'
    default_auto_field = 'django.db.models.BigAutoField'

    # def ready(self):
    #     from .models import Seat
    #     Seat.objects.update(isBooked = False)