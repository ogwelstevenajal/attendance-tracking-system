from django.contrib import admin
from .models import Student, Attendance

# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email', 'course')
    search_fields = ('first_name', 'last_name', 'student_id', 'email')
    list_filter = ('course',)

# Register the Attendance model
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'course_unit', 'duration', 'date')
    search_fields = ('student__first_name', 'student__last_name', 'course', 'course_unit')
    list_filter = ('date',)
