from django.db import models
from Catalog.models import *

# Create your models here.


#класс описывающий книгу

class Book(models.Model):
    name=models.CharField(max_length=100, db_index=True, null=False, blank=False, verbose_name="Название")
    description=models.TextField(max_length=200, editable=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    author=models.ForeignKey(Authors, related_name='author',verbose_name="Авторство", on_delete=models.PROTECT)
    serie=models.ForeignKey(Serie, related_name='series',verbose_name="Серия", on_delete=models.PROTECT)
    genre=models.ForeignKey(Genre, related_name='genres', verbose_name='Жанры', on_delete=models.PROTECT)
    years_to_create=models.DateField(verbose_name='год издания', auto_now=False, default='1950')
    count_sheets=models.PositiveSmallIntegerField(verbose_name='число страниц')
    bindings=models.ForeignKey(Binding, on_delete=models.PROTECT, related_name='bindingse', verbose_name='виды_переплета')
    formate=models.ForeignKey(Format, on_delete=models.PROTECT, related_name='formats', verbose_name='формат')
    ISBN=models.SmallIntegerField(verbose_name='универсальный номер')
    mass=models.SmallIntegerField(verbose_name='вес')
    rating=models.SmallIntegerField(verbose_name='возраст')
    publish_house=models.ForeignKey(Publishing_house, on_delete=models.PROTECT, related_name='publish', verbose_name='Издательства')
    stock = models.PositiveIntegerField(verbose_name="На складе", default=0)
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta():
        ordering = ['name']
        index_together = [
            ['id', 'description']
        
        ]

    def __str__(self):
        return self.name
    
           
