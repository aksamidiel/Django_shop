from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import *
from books.models import Menu
from Catalog.search_form import Search_Author, Search_Form


# Create your views here.


#template_name='some.html'
#temp=5+5
#def get_function(self, **kwargs):
#    context=super().def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["new"] = self.temp
#        return context
     


#для меню
class Menu_view(TemplateView):
    template_name='base_menu.html'

#для вьюхи серий
class SerieDetail(DetailView):
    model=Serie
class SerieList(ListView):
    model=Serie
    #extra_context={'url_detail': 'serie_detail'}

    def get_queryset(self, **kwargs):    # функция поиска
        qs=super().get_queryset(**kwargs)
        search=self.request.GET.get('name', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs 

#для вьюхи жанра
class GenreDetail(DetailView):
    model=Genre
class GenreList(ListView):
    model=Genre
    #extra_context={'url_detail': 'genre_detail'}

    def get_queryset(self, **kwargs):    # функция поиска
        qs=super().get_queryset(**kwargs)
        search=self.request.GET.get('name', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs 

#для вьюхи автора
class AuthorDetail(DetailView):
    model=Authors
class AuthorList(ListView):
    model=Authors
    #form=Search_Author
    #extra_context={'url_detail': 'author_detail'}

    def get_queryset(self, **kwargs):    # функция поиска
        qs=super().get_queryset(**kwargs)
        search=self.request.GET.get('name', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs 
    

#для вьхи издательства
class PublishDetail(DetailView):
    model=Publishing_house

class PublishList(ListView):
    model=Publishing_house

    #extra_context={'url_detail': 'publish_detail'}

    def get_queryset(self, **kwargs):    # функция поиска
        qs=super().get_queryset(**kwargs)
        search=self.request.GET.get('name', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs 


#для вьхи переплета
class BindingDetail(DetailView):
    model=Binding
class BindingList(ListView):
    model=Binding

    #extra_context={'url_detail': 'binding_detail'}

    def get_queryset(self, **kwargs):    # функция поиска
        qs=super().get_queryset(**kwargs)
        search=self.request.GET.get('name', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs 

#для вьхи формата
class FormatDetail(DetailView):
    model=Format
class FormatList(ListView):
    model=Format

    #extra_context={'url_detail': 'format_detail'}

    def get_queryset(self, **kwargs):    # функция поиска
        qs=super().get_queryset(**kwargs)
        search=self.request.GET.get('name', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs 



#######

#create

class Genre_Create(CreateView):    # создание нового жанра
    model=Genre
    fields=['name', 'description']

class Serie_Create(CreateView):   #создание новой серии
    model=Serie
    fields=['name', 'description']
















