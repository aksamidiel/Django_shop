from django import forms
from django.forms import ModelForm
from .models import Genre, Publishing_house, Authors, Serie, Binding, Format

#from django.views.generic import ListView


class Search_Form(forms.Form):   #поисковая форма
    search = forms.CharField(label='Наименование', required=False)


class Author_Form(ModelForm):   #поисковая форма автора по имени
    class Meta:
        model=Authors
        fields=['first_name', 'last_name', 'country']
    #search = forms.CharField(label='Имя', required=False)

class Genre_Form(ModelForm):
    class Meta:
        model=Genre
        fields=['name', 'description']

class Binding_Form(ModelForm):
    class Meta:
        model=Binding
        fields=['bindings', 'description']

class Serie_Form(ModelForm):
    class Meta:
        model=Serie
        fields=['name', 'description']

class Publish_Form(ModelForm):
    class Meta:
        model=Publishing_house
        fields=['name', 'description']

class Format_Form(ModelForm):
    class Meta:
        model=Format
        fields=['formate', 'description']

#class List_Filter(ListView):    #специальный класс основанный на ListView для организации своей логики поиска
   # form = Search_Form

    #def get_context_data(self, *, object_list=None, **kwargs):
       # context = super().get_context_data(**kwargs)
       # if 'search' in self.request.GET:
            #context['form'] = self.form({'search': self.request.GET['search']})
       # else:
           # context['form'] = self.form()
        #return context

    #def get_queryset(self):
        #qs = super().get_queryset()
        #if 'search' in self.request.GET and self.request.GET['search'] != '':
            #name = self.request.GET['search']
            #qs = qs.filter(name__startswith=name)
        #return qs
