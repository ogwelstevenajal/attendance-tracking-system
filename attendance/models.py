from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    student_id = models.CharField(max_length=30, unique=True)
    course = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    course_unit = models.CharField(max_length=100)
    duration = models.DurationField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.student} - {self.course_unit} on {self.date}"
    @classmethod
    def get_attendance_percentage(cls, student_id):      
        total_attendance = cls.objects.filter(student__student_id=student_id).count()
        total_lectures = 30  
        if total_lectures > 0:
            return (total_attendance / total_lectures) * 100
        return 0
