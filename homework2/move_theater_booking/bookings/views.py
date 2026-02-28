from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

    if not seat.is_booked:
        seat.isBooked = True
        seat.save()

        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user
        )

    return redirect('bookingHistory')

@login_required
def bookingHistory(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'bookings/bookingHistory.html', {
        'bookings': bookings
    })

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