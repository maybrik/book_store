# Generated by Django 3.2.9 on 2021-11-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(choices=[('Packed', 'Упакован'), ('Delivering', 'Доставляется'), ('In_progress', 'В обработке'), ('Received', 'Получен')], default='In_progress', max_length=30, verbose_name='Статус заказа'),
        ),
    ]
