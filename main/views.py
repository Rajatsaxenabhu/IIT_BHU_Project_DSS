from django.shortcuts import render

def index(request):
    return render(request, 'main/base.html')

def other(request):
    return render(request, 'other.html')
