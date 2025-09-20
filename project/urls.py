from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),  # default page
    path('register.html/', views.register_view, name='register'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
