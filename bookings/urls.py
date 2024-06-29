#from django.urls import path
#from . import views
#from . import views as booking_views

# urlpatterns = [
   # path('', views.home, name='home'),
   # path('book_lesson/', views.book_lesson, name='book_lesson'),
   # path('view_bookings/', views.view_bookings, name='view_bookings'),
   # path('manage_lessons/', views.manage_lessons, name='manage_lessons'),
   # path('lessons/<int:lesson_id>/', booking_views.lesson_detail, name='lesson_detail'),
   # path('blog/', booking_views.blog, name='blog'),
   # path('faq/', booking_views.faq, name='faq'),
   # path('contact/', booking_views.contact, name='contact'),
#]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_lesson/', views.book_lesson, name='book_lesson'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('manage_lessons/', views.manage_lessons, name='manage_lessons'),
    path('lessons/<int:lesson_id>/', booking_views.lesson_detail, name='lesson_detail'),


]

