from django.contrib import admin

from .models import Genre, Authors, Serie, Publishing_house, Binding_book, Format_book

# Register your models here.

#модель жанра
class GenreAdmin(admin.ModelAdmin):
    list_display=['name', 'description']
    prepopulated_fields={'description':('name',)}

class Authors(admin.ModelAdmin):
    list_display=['first_name', 'last_name']
    prepopulated_fields={'last_name':('first_name',)}

class Serie(admin.ModelAdmin):
    list_display=['name_serie', 'description_name_serie']
    prepopulated_fields={'description_name_serie':('name_serie')}

class Publishing_house(admin.ModelAdmin):
    list_display=['name_publish', 'description_name_publish']
    prepopulated_fields={'description_name_publish':('name_publish')}

class Binding_book(admin.ModelAdmin):
    list_display=['type_binding', 'description_type_binding']
    prepopulated_fields={'description_type_binding':('type_binding')}

class Format_book(admin.ModelAdmin):
    list_display=['type_format', 'description_type_format']
    prepopulated_fields={'description_type_format':('type_format')}


