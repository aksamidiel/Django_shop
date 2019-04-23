"""BookShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Catalog.views import * 
from django.views.generic import TemplateView
from books.models import Menu
from contacts.views import about, index

#admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('ref/author/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    path('ref/binding/<int:pk>', BindingDetail.as_view(), name='binding_detail'),
    path('ref/format/<int:pk>', FormatDetail.as_view(), name='format_detail'),
    path('ref/genre/<int:pk>', GenreDetail.as_view(), name='genre_detail'),
    path('ref/publish/<int:pk>', PublishDetail.as_view(), name='publish_detail'),
    path('ref/serie/<int:pk>', SerieDetail.as_view(), name='serie_detail'),

    #path('ref/author/', AuthorList.as_view()),
    path('ref/binding/', BindingList.as_view(), name='binding_list'),
    path('ref/format/', FormatList.as_view(), name='format_list'),
    path('ref/genre/', GenreList.as_view(), name='genre_list'),
    path('ref/publish/', PublishList.as_view(), name='publish_list'),
    path('ref/serie/', SerieList.as_view(), name='serie_list'),


    path('book/', BookList.as_view(), name='book_list'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),

    path('',Menu.as_view()),   #вывод меню
    path('contacts', about)
   
]
