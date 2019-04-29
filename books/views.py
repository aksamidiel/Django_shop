from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import  Book

# Create your views here.
#контроллер по MVC

#class Menu_List(ListView):
    #queryset=Menu.objects.filter(general_menu__isnull=True)

class BookList(ListView):  #краткая
    model = Book

    def get_queryset(self, **kwargs):
        q_set=super().get_queryset(**kwargs)   #возвращаем родительское определение
        search=self.request.GET.get('name', 0)
        if q_set.filter(name__icontains=search).exists():
            return q_set.filter(name__icontains=search)
        else:
            return q_set
    


class BookDetail(DetailView):   #детальная инфа по книге
    model = Book