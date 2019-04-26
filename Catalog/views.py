from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView

from .models import *
from books.models import Menu
from django.urls import reverse_lazy
from .search_form import *


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
        if qs.filter(name__icontains=search).exists():
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
        if qs.filter(name__icontains=search).exists():
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
            return qs.filter(first_name__icontains=search)
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
        if qs.filter(name__icontains=search).exists():
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
        if qs.filter(bindings__icontains=search).exists():
            return qs.filter(bindings__icontains=search)
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
        if qs.filter(formate__icontains=search).exists():
            return qs.filter(formate__icontains=search)
        else:
            return qs 



#######

#create

class Genre_Create(CreateView):    # создание нового жанра
    model=Genre
    template_name='Create/create_form.html'
    form_class=Genre_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('genre_list')
        return reverse_lazy('genre_create')

    

class Serie_Create(CreateView):   #создание новой серии
    model=Serie
    template_name='Create/create_form.html'
    form_class=Serie_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('serie_list')
        return reverse_lazy('serie_create')

class Author_Create(CreateView):   #создание новых авторов
    model=Authors
    template_name='Create/create_form.html'
    form_class=Author_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('author_list')
        return reverse_lazy('author_create')

class Binding_Create(CreateView):   #создание нового переплета
    model=Binding
    template_name='Create/create_form.html'
    form_class=Binding_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('binding_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('binding_list')
        return reverse_lazy('binding_create')

class Format_Create(CreateView):   #создание нового формата 
    model=Format
    template_name='Create/create_form.html'
    form_class=Format_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('format_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('format_list')
        return reverse_lazy('format_create')


class Publish_Create(CreateView):   #создание нового издательства
    model=Serie
    template_name='Create/create_form.html'
    form_class=Serie_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publish_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('publish_list')
        return reverse_lazy('publish_create')





class Author_Update(UpdateView):
    model = Authors
    template_name = 'Catalog/Update/update_form.html'
    form_class = Author_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('author_list')
        return reverse_lazy('author_update')


class Genre_Update(UpdateView):
    model = Genre
    template_name = 'Catalog/Update/update_form.html'
    form_class = Genre_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('genre_list')
        return reverse_lazy('genre_update')


class Serie_Update(UpdateView):
    model = Serie
    template_name = 'Catalog/Update/update_form.html'
    form_class = Serie_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('serie_list')
        return reverse_lazy('serie_update')


class Publish_Update(UpdateView):
    model = Publishing_house
    template_name = 'Catalog/Update/update_form.html'
    form_class = Publish_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publish_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('publish_list')
        return reverse_lazy('publish_update')


class Binding_Update(UpdateView):
    model = Binding
    template_name = 'Catalog/Update/update_form.html'
    form_class = Binding_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('binding_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('binding_list')
        return reverse_lazy('binding_update')


class Format_Update(UpdateView):
    model = Format
    template_name = 'Catalog/Update/update_form.html'
    form_class = Format_Form

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('format_detail', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('format_list')
        return reverse_lazy('format_update')












