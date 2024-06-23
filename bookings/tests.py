from django.test import TestCase
from django.contrib.auth.models import User
from .models import Lesson, Booking
from datetime import timedelta

class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.lesson = Lesson.objects.create(
            title='Surfing 101',
            description='Beginner lessons',
            date='2024-07-01',
            time='10:00',
            duration=timedelta(hours=1),  # Corrected: Using timedelta for duration
            instructor='John Doe'
        )

    def test_booking_creation(self):
        booking = Booking.objects.create(user=self.user, lesson=self.lesson)
        self.assertEqual(booking.status, 'confirmed')
        self.assertEqual(booking.user.username, 'testuser')
        self.assertEqual(booking.lesson.title, 'Surfing 101')
