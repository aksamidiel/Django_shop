from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):
    context = {'phone': '+375 (44) 123-45-67'}
    return render(request, 'contacts.html', context)

def index(request):
    return render(request, 'hi.html')

