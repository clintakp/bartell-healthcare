from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'About_us.html')

def what_is_chiropractic(request):
    return render(request, 'what_is_chiropractic.html')

def office_hours(request):
    return render(request, 'Office_hours.html')

def services(request):
    return render(request, 'Services.html')

def contact_us(request):
    return render(request, 'contact_us.html')