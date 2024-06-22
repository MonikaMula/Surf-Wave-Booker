from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_lesson, name='book_lesson'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('manage/', views.manage_lessons, name='manage_lessons'),
]
