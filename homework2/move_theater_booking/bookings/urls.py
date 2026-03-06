from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MovieViewSet, SeatViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [

    # REST API endpoints
    path('api/', include(router.urls)),

    # HTML pages
    path('', views.movieList, name='movieList'),
    path('movies/', views.movieList, name='movieList'),
    path('seats/', views.movieList, name='movieList'),
    path('movies/<int:movie_id>/seats/', views.seatBooking, name='seatBooking'),
    path('movies/<int:movie_id>/seats/<int:seat_id>/book/', views.bookSeat, name='bookSeat'),

    path('bookings/', views.bookingHistory, name='bookingHistory'),
    path('clear-bookings/', views.clearBookings, name='clearBookings'),
]
