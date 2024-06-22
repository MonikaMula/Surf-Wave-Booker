from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='confirmed')

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
