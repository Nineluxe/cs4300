# Initialize
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


# API endpoints for "Movie" objects
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# API endpoints for "Seat" objects
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


# API endpoints for "Booking" objects
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


# Renders a list of all available movies
def movieList(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movieList.html', {'movies': movies})


# Renders the seat selection page for a specific movie
@login_required
def seatBooking(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.all()

    return render(request, 'bookings/seatBooking.html', {
        'movie': movie,
        'seats': seats
    })


# Handles the actual seat booking logic for a given movie and seat
# Redirects away if the seat is already taken, otherwise marks it booked and creates a Booking record
@login_required
def bookSeat(request, movie_id, seat_id):
    movie = Movie.objects.get(id=movie_id)
    seat = Seat.objects.get(id=seat_id)

    # send the user back to the seat selection page
    if seat.isBooked:
        return redirect('seatBooking', movie_id=movie.id)

    # Mark the seat as booked
    seat.isBooked = True
    seat.save()

    # Create a Booking record linking the user, movie, and seat together
    Booking.objects.create(
        movie=movie,
        seat=seat,
        user=request.user
    )

    return redirect('bookingHistory')


# Renders the booking history page showing all past bookings for the logged-in user
@login_required
def bookingHistory(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'bookings/bookingHistory.html', {
        'bookings': bookings
    })


# Clears all bookings for the logged-in user
@login_required
def clearBookings(request):
    bookings = Booking.objects.filter(user=request.user)

    # Loop through each booking and release the associated seat
    for booking in bookings:
        seat = booking.seat
        seat.isBooked = False
        seat.save()

    # Bulk delete all booking records for this user
    bookings.delete()

    return redirect('bookingHistory')