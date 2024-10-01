from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def inicial(request):
    return HttpResponse("<h1>”Nome da sua app”</h1>");


def home(request):
    return render(request,'home.html');

