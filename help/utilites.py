from Catalog.models import *
import Catalog.models as model
from books.models import Book



def function_Create():
    print('[1]-создание жанра, [2]-создание автора, [3]-создание серии\
    [4]-создание издательства, [5]-создание переплета [6]-создание формата')

    p=int(input('Введите число для создания словаря в БД: '))

    
    #создание жанра
    if p=='1':

        name=input('Введите название жанра: ')
        description=input('Введите описание жанра: ')

        def create_genre(n, d):

            gen=model.Genre(name=n, description=d)
            gen.save()
            print('В каталоге жанры создан объект {} с ключом={}'.format(gen.name, gen.pk))
    elif p=='2':
    #создание автора

        fir_name=input('Введите имя автора: ')
        last_name=input('Введите фамилию автора: ')
        country=input('Введите страну автора: ')

        def create_author(f_n, l_n, c):
            aut=Authors(first_name=f_n, last_name=l_n, country=c)
            aut.save()
            print('В каталоге Авторы был создан объект {} с ключом={}'.format(aut.first_name, aut.pk))

    elif p=='3':
    #создание серии
        ser=input('Введите серию книг: ')
        descr=input('Введите описание серии: ')

        def create_serie(s, d):
            ser = Serie(name=s, description=d)
            ser.save()
            print('В каталоге Серия был создан объект {} с ключом={}'.format(ser.name, ser.pk))
    elif p=='4':
    #создание издательства

        pubn=input('Введите название издательства: ')
        descr=input('Введите описание издательства: ')

        def create_publ(p_n, desc):
            p_house = Publish(name=n, description=desc)
            p_house.save()
            print('В каталоге Издательства был создан объект {} с ключом={}'.format(p_house.name, p_house.pk))

    elif p=='5':
    #создание переплета
        typ_bind=input('Введите тип переплета: ')
        descr=input('Введите описание переплета: ')


        def create_binding(t, desc):
            bind = Binding(bindings=t, description=desc)
            bind.save()
            print('В каталоге Переплет был создан объект {} с ключом={}'.format(bind.bindings, bind.pk))

    elif p=='6':
    #создание формата

        f_name=input('Введите формат: ')
        descr=input('Введите описание формата: ')

        def create_format(f_n, d_n):
            form = Format(formate=f_n, description=d_n)
            form.save()
            print('В справочнике "Форматы" был создан объект {} с ключом={}'.format(form.formate, obj.pk))
    else:
        print('нет операции, выход')
  #удаление

def deleter(rname, p_k):
    rname.objects.get(pk=p_k).delete()
    print('Из каталога {} был удален объект: {}'.format(rname, p_k))


# функция создания большого количества записей

def creater(count):
    c_list=[]
    for i in range(1, (count+1)):
        ob=Publishing_house(name='издательство'+str(i))
        c_list.append(ob)
    Publishing_house.objects.bulk_create(c_list)
    print('Cоздано {} объектов в каталоге Издательства'.format(count))


# функция подсчета количества записей

def counter(t_name):
    c=t_name.objects.count()
    print("Количество записей в {}: {}".format(t_name, c))



#функция поиска
def searching_f_name(p_name):
    s=Authors.objects.filter(first_name__icontains=p_name).count()
    print('Авторы, фамилии которых содержат фрагмент "{}" - {}'.format(p_name, s))

#create_or_update

def create_updater(name_serie, description_serie):
    s, creat=Serie.objects.update_or_create(
        name=name_serie,

        defaults={'description: ':'some text'}   
    )


#вывод связанных книг

def bind_book(r_name, p_k):
    b = r_name.objects.get(pk=p_k)
    for i in b.books.all():
        print(i)


#создание книги из словаря

def createBook(book):
    b=Book(name=book['name'], description=book['description'], price=book['price'],
    years_to_create=book['years_to_create'], count_sheets=book['count_sheets'],
    ISBN=book['ISBN'], mass=book['mass'], rating=book['rating'], stock=book['stock'],
    available=book['available']
    
    )

    b.genre= Genre.objects.get(name=book[''])





