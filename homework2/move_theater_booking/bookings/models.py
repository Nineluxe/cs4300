from django.db import models
from django.contrib.auth.models import User

# Movie model
class Movie(models.Model):

    # Initialize
    title = models.CharField()
    description = models.TextField()
    releaseDate = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# Seat model
class Seat(models.Model):

    # Initialize
    seatNumber = models.CharField()
    isBooked = models.BooleanField(default=False)

    # Booking status
    def getBooked(self):
        return isBooked
        
    def __str__(self):
        return self.seatNumber

# Booking model
class Booking(models.Model):

    # Initialize
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookingDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seatNumber}"
