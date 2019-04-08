from django.db import models



class Genre(models.Model): # жанр книги
    name=models.CharField("Название жанра", null=False, blank=False, max_length=100, db_index=True, unique=True)   #название жанра
    description=models.CharField("Описание", max_length=300, db_index=True)  #описание жанра


    class Meta:
        ordering=['name']
        verbose_name='Жанр'
        verbose_name_plural='Жанры'

    def __str__(self):
        return self.name


class Authors(models.Model):    #описание авторы
    first_name=models.CharField('Имя', null=False, blank=False, max_length=20, db_index=True)
    last_name=models.CharField('Фамилия', null=True, blank=True, max_length=30, db_index=True, unique=True)
    country=models.CharField("Страна", null=True, blank=True, max_length=20)


    class Meta:
        ordering=['last_name']
        verbose_name='Автор'
        verbose_name_plural='Авторы'
       

    def __str__(self):
        return self.last_name


class Serie(models.Model):   #описание серии

    name=models.CharField('Серия', null=False, blank=False, max_length=50, db_index=True, unique=True)   #название серии
    description=models.CharField('Описание', max_length=300, db_index=True)  #описание серии


    class Meta:
        ordering=['name']
        verbose_name='Серия'
        verbose_name_plural='Серии'

    def __str__(self):
        return self.name


class Publishing_house(models.Model):  #описание издательства
    name=models.CharField('Название',null=False, blank=False, max_length=50, db_index=True, unique=True)   #название издательства
    description=models.CharField('Описание', max_length=300, db_index=True)  #описание издательства


    class Meta:
        ordering=['name']
        verbose_name='Издательство'
        verbose_name_plural='Издательства'

    def __str__(self):
        return self.name

class Binding(models.Model):  #переплет книги
    bindings=models.CharField('Тип переплета',null=False, blank=False, max_length=50, db_index=True, unique=True)   #вид переплета
    description=models.CharField('Описание', max_length=100, db_index=True)  #описание переплета


    class Meta:
        ordering=['bindings']
        verbose_name='Переплет книги'
        verbose_name_plural='Виды переплета'

    def __str__(self):
        return self.bindings


class Format(models.Model):  #переплет книги
    formate=models.CharField('Формат',null=False, blank=False, max_length=50, db_index=True, unique=True)   #формат книги
    description=models.CharField('Описание', max_length=100, db_index=True)  #описание формата


    class Meta:
        ordering=['formate']
        verbose_name='Формат книги'
        verbose_name_plural='Виды форматов'

    def __str__(self):
        return self.formate




        







    


    






    
    
    
       
# Create your models here.
