from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializerClass = MovieSerializer
    # provides get, post, put, delete functionality

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializerClass = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializerClass = BookingSerializer

    # Assigns logged-in user
    def performCreate(self, serializer):
        serializer.save(user=self.request.user)

    def getQueryset(self):
        return Booking.objects.filter(user=self.request.user)


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