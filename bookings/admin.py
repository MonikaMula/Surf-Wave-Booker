from django.contrib import admin
from django import forms
from .models import Lesson, Booking

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ('title', 'date', 'time', 'instructor', 'category', 'max_participants')
    list_filter = ('category', 'date', 'instructor')
    search_fields = ('title', 'description', 'instructor')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'booking_date')
    list_filter = ('lesson', 'booking_date')
    search_fields = ('user__username', 'lesson__title')
