from django import forms
from .models import Booking, Lesson

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['lesson']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'date', 'time', 'duration', 'instructor']
