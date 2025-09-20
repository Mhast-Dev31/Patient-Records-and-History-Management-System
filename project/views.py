from django.shortcuts import render

def login_view(request):
    return render(request, 'index.html')

def register_view(request):
    return render(request, 'register.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
