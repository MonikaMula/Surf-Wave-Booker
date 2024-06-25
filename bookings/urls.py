from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_lesson/', views.book_lesson, name='book_lesson'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('manage_lessons/', views.manage_lessons, name='manage_lessons'),
]
