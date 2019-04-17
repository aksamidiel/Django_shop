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
#from django.urls import path
#from Catalog import views
from django.urls import include, path
from contacts.views import about, index
from Catalog.views import *
#from django.shortcuts import render






urlpatterns = [
    path('admin/', admin.site.urls),
    path('references/author/<int:pk>', AuthorDetail.as_view()),
    path('references/serie/<int:pk>', SerieDetail.as_view()),
    path('references/genre/<int:pk>', GenreDetail.as_view()),
    path('references/format/<int:pk>', FormatDetail.as_view()),
    path('references/publish/<int:pk>', PublishDetail.as_view()),
    path('references/binding/<int:pk>', BindingDetail.as_view()),

    path('',index),
    path('contacts', about)
    #path('refs/serie', SerieDetail.as_view())   #url для view


   
]
