from django.contrib import admin
from .models import *
from books.models import Book



# Register your models here.



#модель серии
class SerieAdmin(admin.ModelAdmin):
    list_display=['name', 'description']
   
    prepopulated_fields={'description':('name',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name']
    prepopulated_fields={'last_name':('first_name',)}

class GenreAdmin(admin.ModelAdmin):
    list_display=['name', 'description']
    prepopulated_fields={'description':('name',)}

class PublishAdmin(admin.ModelAdmin):
    list_display=['name', 'description']
    prepopulated_fields={'description':('name',)}

class BindingAdmin(admin.ModelAdmin):
    list_display=['binding', 'description']
    prepopulated_fields={'description':('binding',)}

class FormatAdmin(admin.ModelAdmin):
    list_display=['formate', 'description']
    prepopulated_fields={'description':('formate',)}


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'description': ('name', )}

admin.site.register(Book, BookAdmin)
admin.site.register(Authors, AuthorAdmin)
admin.site.register(Publishing_house, PublishAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Binding, BindingAdmin)
admin.site.register(Format, FormatAdmin)





