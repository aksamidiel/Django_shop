from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import *
from books.models import Menu
from BookShop.search_form import Search_Author, List_Filter


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
    template_name='books/menu_view.html'

#для вьюхи серий
class SerieDetail(DetailView):
    model=Serie
class SerieList(List_Filter):
    model=Serie
    extra_context={'url_detail': 'serie_detail'}

#для вьюхи жанра
class GenreDetail(DetailView):
    model=Genre
class GenreList(List_Filter):
    model=Genre
    extra_context={'url_detail': 'genre_detail'}

#для вьюхи автора
class AuthorDetail(DetailView):
    model=Authors
class AuthorList(List_Filter):
    model=Authors
    form=Search_Author
    extra_context={'url_detail': 'author_detail'}

#для вьхи издательства
class PublishDetail(DetailView):
    model=Publishing_house

class PublishList(List_Filter):
    model=Publishing_house
    extra_context={'url_detail': 'publish_detail'}


#для вьхи переплета
class BindingDetail(DetailView):
    model=Binding
class BindingList(List_Filter):
    model=Binding
    extra_context={'url_detail': 'binding_detail'}

#для вьхи формата
class FormatDetail(DetailView):
    model=Format
class FormatList(List_Filter):
    model=Format
    extra_context={'url_detail': 'format_detail'}













