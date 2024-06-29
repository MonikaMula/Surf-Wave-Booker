#from django.contrib import admin
#from django.urls import path, include
#from bookings import views as booking_views
#from django.conf import settings
#from django.conf.urls.static import static

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('accounts/', include('allauth.urls')),
 #   path('', booking_views.home, name='home'),
 #   path('book_lesson/', booking_views.book_lesson, name='book_lesson'),
#    path('view_bookings/', booking_views.view_bookings, name='view_bookings'),
 #   path('manage_lessons/', booking_views.manage_lessons, name='manage_lessons'),
#]

#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




from django.contrib import admin
from django.urls import path, include
from bookings import views as booking_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  
    path('', booking_views.home, name='home'),
    path('book_lesson/', booking_views.book_lesson, name='book_lesson'),
    path('view_bookings/', booking_views.view_bookings, name='view_bookings'),
    path('manage_lessons/', booking_views.manage_lessons, name='manage_lessons'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
