# Generated by Django 2.2 on 2019-04-26 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190417_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name'], 'verbose_name': 'книга', 'verbose_name_plural': 'книги'},
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Пункт')),
                ('url_name', models.CharField(max_length=80, verbose_name='Cсылка')),
                ('general_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='general_menu_obj', related_query_name='general_menu_obj', to='books.Menu')),
            ],
        ),
    ]
