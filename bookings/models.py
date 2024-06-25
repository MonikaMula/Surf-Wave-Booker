from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Lesson(models.Model):
    CATEGORY_CHOICES = [
        ('beginner', 'Beginner Surfing'),
        ('intermediate', 'Intermediate Surfing'),
        ('advanced', 'Advanced Surfing'),
        ('mens', 'Men’s Surfing Classes'),
        ('womens', 'Women’s Surfing Classes'),
        ('kids', 'Kids Surfing Lessons'),
        ('junior', 'Junior Surfing Classes'),
        ('family', 'Family Surfing Classes'),
        ('senior', 'Senior Surfing Lessons'),
        ('couples', 'Couples Surfing Classes'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='beginner')
    max_participants = models.IntegerField(default=10)

    def __str__(self):
        return self.title

    def current_participants(self):
        return self.booking_set.count()

    def is_full(self):
        return self.current_participants() >= self.max_participants

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.lesson.is_full():
            raise ValidationError('This lesson is fully booked.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
