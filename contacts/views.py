from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from Catalog.models import Serie

# Create your views here.


def about(request):
    context = {'phone': '+375 (44) 123-45-67'}
    return render(request, 'contacts.html', context)

def index(request):
    return render(request, 'hi.html')


#class SerieDetail(DetailView):   #заготовка для view
   # model=Serie





