from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lesson, Booking
from .forms import BookingForm

@login_required
def book_lesson(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_lesson.html', {'form': form})

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})

@login_required
def manage_lessons(request):
    if request.user.is_staff:
        lessons = Lesson.objects.all()
        return render(request, 'bookings/manage_lessons.html', {'lessons': lessons})
    return redirect('home')
