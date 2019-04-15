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

from contacts.views import about, index

#admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ref/author/<int:pk>', AuthorDetail.as_view()),
    path('ref/binding/<int:pk>', BindingDetail.as_view()),
    path('ref/format/<int:pk>', FormatDetail.as_view()),
    path('ref/genre/<int:pk>', GenreDetail.as_view()),
    path('ref/publish/<int:pk>', PublishDetail.as_view()),
    path('ref/serie/<int:pk>', SerieDetail.as_view()),
    path('',index),
    path('contacts', about)
   
]
