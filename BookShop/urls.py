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
#from books.models import Menu
from books.views import BookList, BookDetail
from Catalog.search_form import *
from django.urls import include   #


#admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Menu_view.as_view(), name='menu'),

    path('book/', include('books.urls')),
    path('ref/', include('Catalog.urls')),

    #path('ref/author/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    #path('ref/binding/<int:pk>', BindingDetail.as_view(), name='binding_detail'),
    #path('ref/format/<int:pk>', FormatDetail.as_view(), name='format_detail'),
    #path('ref/genre/<int:pk>', GenreDetail.as_view(), name='genre_detail'),
    #path('ref/publish/<int:pk>', PublishDetail.as_view(), name='publish_detail'),
    #path('ref/serie/<int:pk>', SerieDetail.as_view(), name='serie_detail'),

    #path('ref/author/', AuthorList.as_view(), name='author_list'),
    #path('ref/binding/', BindingList.as_view(), name='binding_list'),
    #path('ref/format/', FormatList.as_view(), name='format_list'),
    #path('ref/genre/', GenreList.as_view(), name='genre_list'),
    #path('ref/publish/', PublishList.as_view(), name='publish_list'),
    #path('ref/serie/', SerieList.as_view(), name='serie_list'),


    #path('book/', BookList.as_view(), name='book_list'),
    #path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),

    #create_field
    #path('ref/Create/Genre_Create', Genre_Create.as_view(), name='genre_create'),
    #path('ref/Create/Serie_Create', Serie_Create.as_view(), name='serie_create'),
    #path('ref/Create/Binding_Create', Binding_Create.as_view(), name='binding_create'),
    #path('ref/Create/Publish_Create', Publish_Create.as_view(), name='publish_create'),
    #path('ref/Create/Format_Create', Format_Create.as_view(), name='format_create'),
    #path('ref/Create/Author_Create', Author_Create.as_view(), name='author_create'),


    #update fields
    #path('ref/Update/Genre_Update', Genre_Update.as_view(), name='genre_update'),
    #path('ref/Update/Serie_Update', Serie_Update.as_view(), name='serie_update'),
    #path('ref/Update/Binding_Update', Binding_Update.as_view(), name='binding_update'),
    #path('ref/Update/Publish_Update', Publish_Update.as_view(), name='publish_update'),
    #path('ref/Update/Format_Update', Format_Update.as_view(), name='format_update'),
    #path('ref/Update/Author_Update', Author_Update.as_view(), name='author_update'),



    #path('',Menu_view.as_view())  #вывод меню
    #path('contacts', about)

    
]
