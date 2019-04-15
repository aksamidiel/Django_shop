from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.


#template_name='some.html'
#temp=5+5
#def get_function(self, **kwargs):
#    context=super().def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["new"] = self.temp
#        return context
     

#для вьюхи серий
class SerieDetail(DetailView):
    model=Serie
class SerieList(ListView):
    model=Serie

#для вьюхи жанра
class GenreDetail(DetailView):
    model=Genre
class GenreList(ListView):
    model=Genre

#для вьюхи автора
class AuthorDetail(DetailView):
    model=Authors
class AuthorList(ListView):
    model=Authors
#для вьхи издательства
class PublishDetail(DetailView):
    model=Publishing_house
class PublishList(ListView):
    model=Publishing_house

#для вьхи переплета
class BindingDetail(DetailView):
    model=Binding
class BindingList(ListView):
    model=Binding

#для вьхи формата
class FormatDetail(DetailView):
    model=Format
class FormatList(ListView):
    model=Format








