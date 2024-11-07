from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm,AttendanceForm
from .models import Student, Attendance
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, "Account with this email already exists.")
            else:

                user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
                student = form.save(commit=False)
                student.user = user
                student.save()
                return redirect('attendance:login')
    else:
        form = RegistrationForm()
    return render(request, 'attendance/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('attendance:record_attendance')
            else:
                return render(request, 'attendance/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'attendance/login.html', {'form': form})


def record_attendance(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    student = get_object_or_404(Student, user=request.user)
    
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = student
            attendance.save()
            return redirect('attendance:attendance_status')
    else:
        form = AttendanceForm()
    
    return render(request, 'attendance/record_attendance.html', {'form': form})
def attendance_status(request):
    if not request.user.is_authenticated:
        return redirect('login')

    student = Student.objects.get(user=request.user)
    attendance_percentage = Attendance.get_attendance_percentage(student) 
    today = timezone.now().date()
    context = {
        'initials': f"{student.first_name[0]}{student.last_name[0]}",
        'date': today,
        'attendance_percentage': attendance_percentage,
        'eligible': attendance_percentage >= 75,
    }
    return render(request, 'attendance/attendance_status.html', context)

