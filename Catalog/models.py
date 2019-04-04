from django.db import models



class Genre(models.Model): # жанр книги
    name=models.CharField(max_length=100, db_index=True, unique=True)   #название жанра
    description=models.CharField(max_length=300, db_index=True)  #описание жанра


    class Meta:
        ordering=['name']
        verbose_name='Жанр'
        verbose_name_plural='Жанры'

    def __str__(self):
        return self.name


class Authors(models.Model):    #описание авторы
    first_name=models.CharField(max_length=20, db_index=True)
    last_name=models.CharField(max_length=30, db_index=True, unique=True)


    class Meta:
        ordering=['last_name']
        verbose_last_name='Фамилия'
        verbose_last_name_plural='Фамилии'
        verbose_first_name='Имя'
        verbose_first_name_plural='Имена'

    def __str__(self):
        return self.first_name+' '+self.last_name


class Serie(models.Model):   #описание серии

    name_serie=models.CharField(max_length=50, db_index=True, unique=True)   #название серии
    description_name_serie=models.CharField(max_length=300, db_index=True)  #описание серии


    class Meta:
        ordering=['name_serie']
        verbose_name_serie='Серия'
        verbose_name_serie_plural='Серии'

    def __str__(self):
        return self.name_serie


class Publishing_house(models.Model):  #описание издательства
    name_publish=models.CharField(max_length=50, db_index=True, unique=True)   #название серии
    description_name_publish=models.CharField(max_length=300, db_index=True)  #описание серии


    class Meta:
        ordering=['name_publish']
        verbose_name_publish='Издательство'
        verbose_name_publish_plural='Издательства'

    def __str__(self):
        return self.name_publish

class Binding_book(models.Model):  #переплет книги
    type_binding=models.CharField(max_length=50, db_index=True, unique=True)   #вид переплета
    description_type_binding=models.CharField(max_length=100, db_index=True)  #описание переплета


    class Meta:
        ordering=['type_binding']
        verbose_type_binding='Переплет книги'
        verbose_type_binding_plural='Виды переплета'

    def __str__(self):
        return self.type_binding


class Format_book(models.Model):  #переплет книги
    type_format=models.CharField(max_length=50, db_index=True, unique=True)   #формат книги
    description_type_format=models.CharField(max_length=100, db_index=True)  #описание формата


    class Meta:
        ordering=['type_format']
        verbose_type_format='Формат книги'
        verbose_type_format_plural='Виды форматов'

    def __str__(self):
        return self.type_format




class Book(models.Model):    #модель товара(книга)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    description_book=models.CharField(max_length=500, verbose_name="Описание")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение книги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    author = models.ForeignKey(Authors, related_name='authors', verbose_name="Автор")
    serie = models.ForeignKey(Serie, related_name="serie",verbose_name="Серия")
    genre = models.ForeignKey(Genre, related_name="genre",verbose_name="Жанр")
    date_of_publication = models.DateField(verbose_name="Год издания")
    count_shiets = models.PositiveIntegerField(verbose_name="Число страниц")
    binding=models.ForeignKey(Binding_book, related_name="binding_book",verbose_name="Переплет")
    format_b=models.ForeignKey(Format_book, related_name="format_book",verbose_name="Формат")
    ISBN=models.PositiveIntegerField(verbose_name="Штрихкод")
    weight=models.PositiveIntegerField(verbose_name="Вес")
    ages=models.PositiveIntegerField(verbose_name="Возрастная группа")
    pub_house=models.ForeignKey(Publishing_house, related_name="publish_house",verbose_name="Издательство")
    stock = models.PositiveIntegerField(verbose_name="Число книг на складе")
    available = models.BooleanField(default=True, verbose_name="Доступен для заказа")
    rating=models.models.PositiveSmallIntegerField(verbose_name="Рейтинг")
    created = models.DateTimeField(auto_now_add=True)   #дата добавления
    updated = models.DateTimeField(auto_now=True)   #дата обновления


    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'description_book']
        ]


    


    






    
    
    
       
# Create your models here.
