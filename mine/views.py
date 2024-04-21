from django.http import request
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def services(render):
    return render(request, 'services.html')
def projectpage(request):
    return render(request, 'projectpage.html')
