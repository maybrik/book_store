# Generated by Django 3.2.9 on 2021-11-09 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('about', models.CharField(max_length=500)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('author', models.ManyToManyField(related_name='Автор', to='stock.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.TextField(max_length=200, verbose_name='Издательство')),
                ('city', models.TextField(max_length=100, verbose_name='Город')),
                ('license', models.CharField(max_length=19, verbose_name='Номер лицензии')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('date_of_order', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Packed', 'Упакован'), ('Received', 'Получен'), ('Delivering', 'Доставляется'), ('In_progress', 'В обработке')], default='In_progress', max_length=30, verbose_name='Статус заказа')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.book')),
                ('publisher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.publisher')),
            ],
        ),
    ]
