from behave import given, when, then
from bookings.models import Movie, Seat, Booking
from django.contrib.auth.models import User
import datetime

@given('a movie "{title}" exists')
def step_impl(context, title):
    context.movie = Movie.objects.create(
        title=title,description="",releaseDate=datetime.date(2026,3,5),duration=120
        )

@given('seat "{seat}" is available')
def step_impl(context, seat):
    context.seat = Seat.objects.create(seatNumber=seat)

@when('the user books seat "{seat}"')
def step_impl(context, seat):
    user = User.objects.create(username="Bryce")

    Booking.objects.create(
        user=user,
        movie=context.movie,
        seat=context.seat
    )

    context.seat.isBooked = True
    context.seat.save()

@then('the seat should be marked as booked')
def step_impl(context):
    assert context.seat.isBooked == True
