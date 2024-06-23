from django.contrib import admin
from .models import Lesson, Booking

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'instructor', 'current_participants', 'is_full')
    search_fields = ('title', 'instructor')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'booking_date')
    search_fields = ('user__username', 'lesson__title')
    list_filter = ('booking_date',)
