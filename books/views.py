from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Menu, Book

# Create your views here.


class Menu_List(ListView):
    queryset=Menu.objects.filter(general_menu__isnull=True)

class BookList(ListView):  #краткая
    model = Book


class BookDetail(DetailView):   #детальная инфа по книге
    model = Book