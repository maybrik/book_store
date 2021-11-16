from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    deathdate = models.DateField()
    about = models.CharField(max_length=500)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def str(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    CLASSICS = 'Classics'
    DETECTIVE = 'Detective'
    ADVENTURE = 'Adventure'
    FANTASY = 'Fantasy'
    ROMANCE = 'Romance'
    POETRY = 'Poetry'

    CHOICE_GROUP = {
        (CLASSICS, 'Classics'),
        (DETECTIVE, 'Detective'),
        (ADVENTURE, 'Adventure'),
        (FANTASY, 'Fantasy'),
        (ROMANCE, 'Romance'),
        (POETRY, 'Poetry')
    }

    name = models.CharField('Название книги', max_length=100)
    description = models.TextField('Описание книги', max_length=350)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=10)
    author = models.ManyToManyField(Author, 'Автор')
    genre = models.CharField('Жанр', max_length=20, choices=CHOICE_GROUP, default=CLASSICS)
    rating = models.FloatField('Рейтинг')
    available = models.BooleanField(default=True)

    def _str_(self):
        return f'{self.name}'