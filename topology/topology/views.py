from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("<h1>Welcome to the Home page</h1>")
    return render(request, 'dashboard.html')

def about(request):
    #return HttpResponse('<h1>Hello About page!</h1>')
    return render(request, 'about.html')