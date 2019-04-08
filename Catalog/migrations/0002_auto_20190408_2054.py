# Generated by Django 2.2 on 2019-04-08 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='binding',
            options={'ordering': ['bindings'], 'verbose_name': 'Переплет книги', 'verbose_name_plural': 'Виды переплета'},
        ),
        migrations.AlterModelOptions(
            name='format',
            options={'ordering': ['formate'], 'verbose_name': 'Формат книги', 'verbose_name_plural': 'Виды форматов'},
        ),
        migrations.RenameField(
            model_name='binding',
            old_name='binding',
            new_name='bindings',
        ),
        migrations.RenameField(
            model_name='format',
            old_name='format',
            new_name='formate',
        ),
    ]