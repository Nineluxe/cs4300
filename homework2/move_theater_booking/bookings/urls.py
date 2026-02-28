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
    path('movies-file/', views.moviesListTest, name='movies'),
    router.urls
]
