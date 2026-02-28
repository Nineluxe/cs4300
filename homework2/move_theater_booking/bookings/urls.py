from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('seats', SeatViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('movies/', views.movieList, name='movieList'),
    path('movies/<int:movie_id>/seats/', views.seatBooking, name='seatBooking'),
    path('movies/<int:movie_id>/seats/<int:seat_id>/book/', views.bookSeat, name='bookSeat'),
    path('history/', views.bookingHistory, name='bookingHistory'),
]