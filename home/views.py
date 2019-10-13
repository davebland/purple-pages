from django.shortcuts import render

def home(request):
    """ Generate Application Home Page """
    return render(request, 'home.html')