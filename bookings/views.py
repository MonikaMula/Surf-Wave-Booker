#from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
#from .forms import BookingForm
#from .models import Lesson, Booking
#from django.shortcuts import render, get_object_or_404
#from .models import Lesson

#@login_required
#def book_lesson(request):
 #   if request.method == 'POST':
 #       form = BookingForm(request.POST)
  #      if form.is_valid():
  #          booking = form.save(commit=False)
  #          booking.user = request.user
    #        booking.save()
    #        return redirect('view_bookings')
  #  else:
    #    form = BookingForm()
   # return render(request, 'bookings/book_lesson.html', {'form': form})

#@login_required
#def view_bookings(request):
 #   bookings = Booking.objects.filter(user=request.user)
  #  return render(request, 'bookings/view_bookings.html', {'bookings': bookings})

#@login_required
#def manage_lessons(request):
 #   if request.user.is_staff:
   #     lessons = Lesson.objects.all()
   #     return render(request, 'bookings/manage_lessons.html', {'lessons': lessons})
    #return redirect('home')

#def home(request):
 #   return render(request, 'home.html')
 
 
 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Lesson, Booking
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render


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

def home(request):
    return render(request, 'home.html')

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
