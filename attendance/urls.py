from django.urls import path
from . import views
app_name='attendance'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
   
    path('record_attendance/', views.record_attendance, name='record_attendance'),
    path('attendance_status/',views. attendance_status, name='attendance_status'),
]
