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
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', views.seat_booking, name='seat_booking'),
    path('movies/<int:movie_id>/seats/<int:seat_id>/book/', views.book_seat, name='book_seat'),
    path('history/', views.booking_history, name='booking_history'),
]