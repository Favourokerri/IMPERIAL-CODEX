from django.shortcuts import render

# Create your views here.
def index(request):
    """view function for index.html"""
    return render(request, 'index.html')

def attendance(request):
    """view function for the attendance"""
    return render(request, 'attendance.html')

def enroll(request):
    """view function for the enroll"""
    return render(request, 'enroll.html')

def about(request):
    """view function for index.html"""
    return render(request, 'about.html')

def services(request):
    """view function for the attendance"""
    return render(request, 'services.html')

def contact(request):
    """view function for index.html"""
    return render(request, 'contact.html')

def courses(request):
    """view function for our courses"""
    return render(request, 'courses.html')
