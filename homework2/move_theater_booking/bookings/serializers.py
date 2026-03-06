from rest_framework import serializers
from .models import Movie, Seat, Booking

# Serializers convert the models.py objects into JSON
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# Seat Serializer
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '_all__'

# Booking serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '_all__'
        readOnlyFields = ['user', 'bookingDate'] # prevents user from changing these fields