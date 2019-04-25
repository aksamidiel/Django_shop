from django.contrib import admin
from .models import *




# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['name', 'price', 'years_to_create']
    list_filter=['name', 'author', 'serie', 'genre']
    #search_fields=[field.name for field in Book._meta.fields]

    class Meta:
        model=Book
