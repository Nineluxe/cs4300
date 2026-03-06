from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # # API booking logic
    # def perform_create(self, serializer):

    #     seat = serializer.validated_data['seat']

    #     # Check if the seat is already booked
    #     if seat.isBooked:
    #         raise Exception("This seat is already booked.")

    #     #if not seat.isBooked:
    #     # Mark the seat as booked
    #     seat.isBooked = True
    #     seat.save()

    #     serializer.save(user=self.request.user)


    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

def movieList(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movieList.html', {'movies': movies})

@login_required
def seatBooking(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.all()

    return render(request, 'bookings/seatBooking.html', {
        'movie': movie,
        'seats': seats
    })

@login_required
def bookSeat(request, movie_id, seat_id):
    movie = Movie.objects.get(id=movie_id)
    seat = Seat.objects.get(id=seat_id)

    if seat.isBooked:
        return redirect('seatBooking', movie_id=movie.id)

    seat.isBooked = True
    seat.save()

    Booking.objects.create(
        movie=movie,
        seat=seat,
        user=request.user
    )

    # Debug
    print("Booking seat:", seat.seatNumber)
    print("Current status:", seat.isBooked)

    return redirect('bookingHistory')

@login_required
def bookingHistory(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'bookings/bookingHistory.html', {
        'bookings': bookings
    })


# Finds the bookings of the logged-in user
# Frees the seats by setting isBooked to False
# Deletes the booking records
# Finally redirects back to the booking history page
@login_required
def clearBookings(request):
    bookings = Booking.objects.filter(user=request.user)

    for booking in bookings:
        seat = booking.seat
        seat.isBooked = False
        seat.save()

    bookings.delete()

    return redirect('bookingHistory')

# # Create your views here.
# def moviesListTest(request):
#     movies = []

#     # Open the file
#     with open("movies.txt", "r") as file:
#         for line in file:

#             # Split the data inside the file
#             title, director, year, duration = line.strip().split("|")

#             # Create the structured data "packet"
#             movies.append(
#                 {
#                     "title": title,
#                     "director": director,
#                     "year": year,
#                     "duration": duration
#                 }
#             )

#     # Pass the data to a template
#     # Simulates what a database query would normally return
#     return render(request, "bookings/moviesList.html", {"movies": movies})