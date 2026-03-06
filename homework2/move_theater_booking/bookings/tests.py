from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
import datetime
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.

# Test the movie generation
class MovieModelTest(TestCase):

    def testCreateMovie(self):
        movie = Movie.objects.create(
            title="Forrest Gump", description="", releaseDate=datetime.date(1994, 1, 1),duration=142)
        self.assertEqual(movie.title, "Forrest Gump")

# Verify that a new seat automatically defaults to not booked
class SeatModelTest(TestCase):

    def testSeatDefault(self):
        seat = Seat.objects.create(seatNumber="A1")
        self.assertFalse(seat.isBooked)

# Verify the integrity of the entire booking pipeline
class BookingTest(TestCase):

    def testBookingCreation(self):
        user = User.objects.create_user(username="Bryce", password="test")

        movie = Movie.objects.create(
            title="Forrest Gump", description="", releaseDate=datetime.date(1994, 1, 1),duration=142)
        seat = Seat.objects.create(seatNumber = "A1")

        booking = Booking.objects.create(
            user=user,
            movie=movie,
            seat=seat
        )

        self.assertEqual(booking.movie.title, "Forrest Gump")
        self.assertEqual(booking.seat.seatNumber, "A1")
        self.assertEqual(booking.user.username, "Bryce")

# API Test
class APITests(APITestCase):

    # Initialize
    def setUp(self):
        self.user = User.objects.create_user(username="Bryce", password="test")
        self.client.login(username="Bryce", password="test")

        self.movie = Movie.objects.create(
            title="Forrest Gump", description="", releaseDate=datetime.date(1994, 1, 1),duration=142)
        self.seat = Seat.objects.create(seatNumber="A1")

    # Verify movie listings
    def testGetMovies(self):
        response = self.client.get('/api/movies/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Verify movie booking
    def testBookSeat(self):
        user = User.objects.create_user(username="Tester", password="test")
        self.client.login(username="Tester", password="test")

        movie = Movie.objects.create(
            title="Forrest Gump", description="", releaseDate=datetime.date(1994, 1, 1),duration=142)

        seat = Seat.objects.create(seatNumber="A1")

        response = self.client.post('/api/bookings/', {
            "movie": movie.id,
            "seat": seat.id
        })
        
        self.assertEqual(response.status_code, 200)

    # Verify that double booking is handled properly
    def testCannotDoubleBookSeat(self):
        self.seat.isBooked = True
        self.seat.save()

        response = self.client.post('/api/bookings/', {
            "movie": self.movie.id,
            "seat": self.seat.id
        })

        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)