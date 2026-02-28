from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField()
    description = models.TextField()
    releaseDate = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Seat(models.Model):
    seatNumber = models.CharField()
    isBooked = models.BooleanField(default=False)

    def __str__(self):
        return self.seatNumber


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookingDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seatNumber}"
