from django.shortcuts import render

# Create your views here.

def inicial(request):
    return render(request,'paginas/inicial.html')
