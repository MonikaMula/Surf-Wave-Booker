from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking, Lesson

@login_required
def book_lesson(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            lesson = form.cleaned_data['lesson']
            if lesson.is_full():
                messages.error(request, 'Sorry, this lesson is fully booked.')
                return redirect('book_lesson')
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'You have successfully booked the lesson!')
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_lesson.html', {'form': form})

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'view_bookings.html', {'bookings': bookings})

@login_required
def manage_lessons(request):
    if request.user.is_staff:
        lessons = Lesson.objects.all()
        return render(request, 'manage_lessons.html', {'lessons': lessons})
    return redirect('home')
